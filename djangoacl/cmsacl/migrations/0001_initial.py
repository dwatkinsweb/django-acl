# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='Action Name')),
                ('groups', models.ManyToManyField(related_name='cms_action_pages', verbose_name='Groups', to='auth.Group', blank=True)),
                ('page', models.OneToOneField(related_name='action', verbose_name='Action Name', to='cms.Page', max_length=20)),
                ('users', models.ManyToManyField(related_name='cms_action_pages', verbose_name='Users', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
    ]
