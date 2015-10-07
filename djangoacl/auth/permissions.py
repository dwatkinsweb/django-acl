from djangoacl.models import Action


def get_user_group_acl(user):
    if not hasattr(user, '_group_acl_cache'):
        if user.is_superuser:
            actions = Action.objects.all()
        else:
            actions = Action.objects.filter(groups__user=user)
        actions = actions.values_list('name').order_by()
        user._group_acl_cache = set([name for name, in actions])
    return user._group_acl_cache


def get_user_acl(user):
    if not hasattr(user, '_acl_cache'):
        user._acl_cache = set([a.name for a in user.actions.select_related()])
        user._acl_cache.update(get_user_group_acl(user))
    return user._acl_cache
