==========
DJANGO-ACL
==========

Django has a built in permissions system, but all the permissions are more directly related to models. This is meant to
extend that system by adding permissions, or actions, not related specifically to models.

This also adds an ACL aspect to Django-CMS as an optional feature. See Documentation (cmsacl) below.

*************************
Documentation (djangoacl)
*************************

Add to ``INSTALLED APPS``
=========================
    Add the module to your installed apps.

    .. code-block:: python

        INSTALLED_APS = (
            ...
            'djangoacl'
        )

Authentication Backend
======================
    Add the new authentication backend to ``AUTHENTICATION_BACKENDS`` in settings.py

    .. code-block:: python

        AUTHENTICATION_BACKENDS = (
            ...
            'djangoacl.auth.backends.ACLBackend',
        )

Run migrations
==============
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

*************************
Documentation (djangoacl)
*************************

Add to ``INSTALLED APPS``
=========================
    Add the module to your installed apps.

    .. code-block:: python

        INSTALLED_APS = (
            ...
            'djangoacl.cmsacl'
        )

Register the MenuModifier
=========================
    You will want to put this somewhere you know will be run before as soon as possible. I would recommend in your
    urls or somewhere similar. This will keep the pages from showing up in the menu if the user does not have
    permissions.

    .. code-block:: python

        from menus.menu_pool import menu_pool
        menu_pool.register_modifier(ACLModifier)

Add the new Middleware
======================
    Add the new middleware to ``MIDDLEWARE_CLASSES`` in settings.py

    .. code-block:: python

        MIDDLEWARE_CLASSES = (
            ...
            'djangoacl.cmsacl.middleware.CMSPageACL',
        )

Run migrations
==============
    .. code-block:: bash

        $ python manage.py migrate cmsacl

Add the action
==============
    Go to http://yoursite/admin/cmsacl/action/add/ and add the action.

    Give the action a name. This can be pretty much anything you want but recommend no spaces or special characters.
    Also probably best not to use anything that matches then normal permission patters such as `<action>_<model>` or
    `<model>.<action>`

    Attach a page to the action.

    Make sure to add any related users or groups.
