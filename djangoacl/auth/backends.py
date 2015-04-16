from django.contrib.auth.backends import ModelBackend
from djangoacl.models import Action


class ACLBackend(ModelBackend):
    def get_group_permissions(self, user_obj, obj=None):
        if user_obj.is_anonymous() or obj is not None:
            return set()
        if not hasattr(user_obj, '_group_acl_cache'):
            if user_obj.is_superuser:
                actions = Action.objects.all()
            else:
                actions = Action.objects.filter(groups__user=user_obj)
            actions = actions.values_list('name').order_by()
            user_obj._group_acl_cache = set([name for name, in actions])
        return user_obj._group_acl_cache
    
    def get_all_permissions(self, user_obj, obj=None):
        if user_obj.is_anonymous() or obj is not None:
            return set()
        if not hasattr(user_obj, '_acl_cache'):
            user_obj._acl_cache = set([a.name for a in user_obj.actions.select_related()])
            user_obj._acl_cache.update(self.get_group_permissions(user_obj))
        return user_obj._acl_cache



