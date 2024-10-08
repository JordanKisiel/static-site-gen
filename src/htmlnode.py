class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""

        props_list = self.props.items()
        sorted_props = sorted(props_list, key=lambda x: x[0])
        prop_str = ""

        for prop in sorted_props:
            key = prop[0]
            value = prop[1]
            prop_str += f" {key}='{value}'"
        
        return prop_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        

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
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes must have values")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"