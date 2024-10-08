from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must have tag")
        if self.children == None or len(self.children) == 0:
            raise ValueError("Parent node must have at least one child")

        # base case for recursive call below is when
        # node is a leafnode
        html_str = ""
        for node in self.children:
            html_str += node.to_html()

        return f"<{self.tag}>{html_str}</{self.tag}>"