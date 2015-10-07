from cms.models import Page
from menus.base import Modifier

from .permissions import user_has_cms_page_permissions


class ACLModifier(Modifier):
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        final_nodes = []
        for node in nodes:
            node_page = Page.objects.get(pk=node.id)
            if user_has_cms_page_permissions(request.user, node_page):
                final_nodes.append(node)
            else:
                if node.parent and node in node.parent.children:
                    node.parent.children.remove(node)

        return final_nodes
