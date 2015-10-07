from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CMSAction(models.Model):
    name = models.CharField(verbose_name=_('Action Name'), max_length=20, unique=True)
    page = models.OneToOneField('cms.Page', related_name='action', verbose_name=_('Pages'),
                                limit_choices_to={'publisher_is_draft': False})
    users = models.ManyToManyField('auth.User', verbose_name=_('Users'), related_name='cms_action_pages', blank=True)
    groups = models.ManyToManyField('auth.Group', verbose_name=_('Groups'), related_name='cms_action_pages', blank=True)
