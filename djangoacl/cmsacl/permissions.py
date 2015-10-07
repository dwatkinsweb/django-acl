from .models import CMSAction


def get_user_group_acl(user):
    if not hasattr(user, '_group_acl_cms_cache'):
        if user.is_superuser:
            actions = CMSAction.objects.all()
        else:
            actions = CMSAction.objects.filter(groups__user=user)
        actions = actions.values_list('name').order_by()
        user._group_acl_cms_cache = set([name for name, in actions])
    return user._group_acl_cms_cache


def get_user_acl(user):
    if not hasattr(user, '_acl_cms_cache'):
        user._acl_cms_cache = set([a.name for a in user.cms_action_pages.select_related()])
        user._acl_cms_cache.update(get_user_group_acl(user))
    return user._acl_cms_cache


def user_has_cms_page_permissions(user, page):
    if user.is_superuser:
        return True
    try:
        action = CMSAction.objects.get(page=page)
        return action.name in get_user_acl(user)
    except CMSAction.DoesNotExist:
        # Pages are public by default
        return True
