from django.contrib.auth.models import User
from django.test import TransactionTestCase


class ACLBackendTest(TransactionTestCase):
    fixtures = ['testacl.json']

    def test_user_has_perm_from_group(self):
        user = User.objects.get(pk=1)
        self.assertTrue(user.has_perm('testaction1'))

    def test_user_has_perm_from_group2(self):
        user = User.objects.get(pk=3)
        self.assertTrue(user.has_perm('testaction2'))

    def test_user_lacks_perm_from_group(self):
        user = User.objects.get(pk=2)
        self.assertFalse(user.has_perm('testaction2'))

    def test_user_lacks_perm_from_group2(self):
        user = User.objects.get(pk=4)
        self.assertFalse(user.has_perm('testaction1'))

    def test_user_has_perm(self):
        user = User.objects.get(pk=5)
        self.assertTrue(user.has_perm('testaction1'))

    def test_user_has_perm2(self):
        user = User.objects.get(pk=6)
        self.assertTrue(user.has_perm('testaction2'))

    def test_user_lacks_perm(self):
        user = User.objects.get(pk=5)
        self.assertFalse(user.has_perm('testaction2'))

    def test_user_lacks_perm2(self):
        user = User.objects.get(pk=6)
        self.assertFalse(user.has_perm('testaction1'))