==========
DJANGO-ACL
==========

Django has a built in permissions system, but all the permissions are more directly related to models. This is meant to
extend that system by adding permissions, or actions, not related specifically to models.

*************
Documentation
*************

Add to ``INSTALLED APPS``
=========================
    Add the module to your installed apps.

    .. code-block:: python

        INSTALLED_APS = (
            ...
            'djangoacl'
        )

Template Loader
===============
    Add the new authentication backend to ``AUTHENTICATION_BACKENDS`` in settings.py

    .. code-block:: python

        TEMPLATE_LOADERS = (
            'skin.template.loaders.filesystem.Loader',
            'skin.template.loaders.app_directories.Loader',
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )

Run migrations
==============
    If you have south, run migrations

    .. code-block:: bash

        $ python manage.py migrate djangoacl

Add the action
==============
    Go to http://yoursite/admin/djangoacl/action/add/ and add the action.

    Give the action a name. This can be pretty much anything you want but recommend no spaces or special characters.
    Also probably best not to use anything that matches then normal permission patters such as `<action>_<model>` or
    `<model>.<action>`

    Make sure to add any related users or groups.

Request Permission
==================

    Request permission in the normal way using the ``permission_required`` decorator. See
    https://docs.djangoproject.com/en/1.8/topics/auth/default/#the-permission-required-decorator
