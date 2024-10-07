class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        text_matches = self.text == text_node.text
        type_matches = self.text_type == text_node.text_type
        url_matches = self.url == text_node.url
        return text_matches and type_matches and url_matches

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        