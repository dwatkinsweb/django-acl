from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Action(models.Model):
    name = models.CharField(verbose_name=_('Action Name'), max_length=20, unique=True)
    users = models.ManyToManyField('auth.User', verbose_name=_('Users'), related_name='actions')
    groups = models.ManyToManyField('auth.Group', verbose_name=_('Groups'), related_name='actions')