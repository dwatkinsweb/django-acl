from cms.api import create_page
from cms.test_utils.testcases import BaseCMSTestCase
from django.template import Template, RequestContext
from menus.menu_pool import menu_pool

from django.contrib.auth.models import User, Group
from django.test import TransactionTestCase, RequestFactory
from djangoacl.cmsacl.menu import ACLModifier

from djangoacl.cmsacl.models import CMSAction


class ACLBackendTest(BaseCMSTestCase, TransactionTestCase):
    def setUp(self):
        self.simple_user = User.objects.create(username='simple_user', email='simple_user@test.insuremonkey.com',
                                               password='simple_user')
        self.advanced_user = User.objects.create(username='advanced_user', email='advanced_user@test.insuremonkey.com',
                                                 password='advanced_user')
        self.superuser = User.objects.create(username='super_user', email='super_user@test.insuremonkey.com',
                                             password='super_user', is_superuser=True)
        self.advanced_group = Group.objects.create(name='advanced_group')
        self.advanced_group.user_set.add(self.advanced_user)

        page_defaults = {
            'template': 'menu_test.html',
            'language': 'en-us',
        }
        with self.settings(CMS_PERMISSION=False):
            self.p1 = create_page('P1', published=True, in_navigation=True, **page_defaults)
            self.p2 = create_page('P2', published=True, in_navigation=True, parent=self.p1, **page_defaults)
            self.p3 = create_page('P3', published=True, in_navigation=True, parent=self.p2, **page_defaults)

            self.p4 = create_page('P4', published=True, in_navigation=True, **page_defaults)
            self.p5 = create_page('P5', published=True, in_navigation=True, parent=self.p4, **page_defaults)

            self.p6 = create_page('P6', published=True, in_navigation=False, **page_defaults)
            self.p7 = create_page('P7', published=True, in_navigation=True, parent=self.p6, **page_defaults)
            self.p8 = create_page('P8', published=True, in_navigation=True, parent=self.p6, **page_defaults)

        p1_action = CMSAction.objects.create(name='p1_action', page=self.p1.publisher_public)
        p1_action.users.add(self.simple_user)
        p1_action.groups.add(self.advanced_group)

        p2_action = CMSAction.objects.create(name='p2_action', page=self.p2.publisher_public)
        p2_action.users.add(self.simple_user)

        p3_action = CMSAction.objects.create(name='p3_action', page=self.p3.publisher_public)

        p4_action = CMSAction.objects.create(name='p4_action', page=self.p4.publisher_public)
        p4_action.users.add(self.simple_user)
        p4_action.groups.add(self.advanced_group)

        p5_action = CMSAction.objects.create(name='p5_action', page=self.p5.publisher_public)
        p5_action.groups.add(self.advanced_group)

        p6_action = CMSAction.objects.create(name='p6_action', page=self.p6.publisher_public)
        p6_action.groups.add(self.advanced_group)

        p7_action = CMSAction.objects.create(name='p7_action', page=self.p7.publisher_public)
        p7_action.users.add(self.simple_user)

        p8_action = CMSAction.objects.create(name='p8_action', page=self.p8.publisher_public)
        p8_action.groups.add(self.advanced_group)

        menu_pool.register_modifier(ACLModifier)

    def test_user_permissions(self):
        context = self.get_context('/', self.p4)
        context['request'].user = self.simple_user
        expected_html = '''
        <li class="child selected">
            <a href="/"></a>
            <ul>
                <li class="child descendant">
                    <a href="/p2/">P2</a>
                </li>
            </ul>
        </li>
        <li class="child sibling">
            <a href="/p4/">P4</a>
        </li>
        '''

        tpl = Template("{% load menu_tags %}{% show_menu 0 100 100 100 %}")
        html = tpl.render(context)
        nodes = context['children']
        self.assertEqual(len(nodes), 2)
        self.assertEqual(len(nodes[0].children), 1)
        self.assertEqual(len(nodes[0].children[0].children), 0)
        self.assertEqual(len(nodes[1].children), 0)
        self.assertHTMLEqual(html, expected_html)

    def test_group_permissions(self):
        context = self.get_context('/')
        context['request'].user = self.advanced_user
        expected_html = '''
        <li class="child selected">
            <a href="/"></a>
        </li>
        <li class="child sibling">
            <a href="/p4/">P4</a>
            <ul>
                <li class="child">
                    <a href="/p4/p5/">P5</a>
                </li>
            </ul>
        </li>
        '''

        tpl = Template("{% load menu_tags %}{% show_menu 0 100 100 100 %}")
        html = tpl.render(context)
        nodes = context['children']
        self.assertEqual(len(nodes), 2)
        self.assertEqual(len(nodes[0].children), 0)
        self.assertEqual(len(nodes[1].children), 1)
        self.assertHTMLEqual(html, expected_html)

    def test_superuser_permissions(self):
        context = self.get_context('/')
        context['request'].user = self.superuser
        expected_html = '''
        <li class="child selected">
            <a href="/"></a>
            <ul>
                <li class="child descendant">
                    <a href="/p2/">P2</a>
                    <ul>
                        <li class="child descendant">
                            <a href="/p2/p3/">P3</a>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>
        <li class="child sibling">
            <a href="/p4/">P4</a>
            <ul>
                <li class="child">
                    <a href="/p4/p5/">P5</a>
                </li>
            </ul>
        </li>
        '''

        tpl = Template("{% load menu_tags %}{% show_menu 0 100 100 100 %}")
        html = tpl.render(context)
        nodes = context['children']
        self.assertEqual(len(nodes), 2)
        self.assertEqual(len(nodes[0].children), 1)
        self.assertEqual(len(nodes[0].children[0].children), 1)
        self.assertEqual(len(nodes[1].children), 1)
        self.assertHTMLEqual(html, expected_html)

