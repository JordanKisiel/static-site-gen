import unittest
from src.htmlnode import HTMLNode

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

    def test_empty_props(self):
        props = {}

        node = HTMLNode("p", "My paragraph", [], props)

        self.assertEqual(
            "", node.props_to_html()
        )

    def test_to_html_error(self):
        node = HTMLNode("img", "my raw text", [], {
            "src": "path/to/source.jpg",
            "alt": "my alt text"
        })

        self.assertRaises(NotImplementedError, node.to_html)

if __name__ == "__main__":
    unittest.main()

