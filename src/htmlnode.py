class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
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
        
