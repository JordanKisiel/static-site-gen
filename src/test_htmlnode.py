import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode("a", "My link", [], props)

        self.assertEqual(
            f" href='{props['href']}' target='{props['target']}'",
            node.props_to_html()
        )