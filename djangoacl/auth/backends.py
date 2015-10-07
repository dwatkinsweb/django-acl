from django.contrib.auth.backends import ModelBackend
from djangoacl.auth.permissions import get_user_group_acl, get_user_acl


class ACLBackend(ModelBackend):
    def get_group_permissions(self, user_obj, obj=None):
        if user_obj.is_anonymous() or obj is not None:
            return set()
        return get_user_group_acl(user_obj)
    
    def get_all_permissions(self, user_obj, obj=None):
        if user_obj.is_anonymous() or obj is not None:
            return set()
        return get_user_acl(user_obj)
