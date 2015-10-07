from django.core.exceptions import PermissionDenied
from djangoacl.auth.permissions import user_has_cms_page_permissions


class CMSPageACL(object):
    def process_request(self, request):
        if not user_has_cms_page_permissions(request.user, request.current_page):
            raise PermissionDenied('You do not have access to view this page.')
