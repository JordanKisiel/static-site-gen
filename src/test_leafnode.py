import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_no_value_error(self):
        leaf_node = LeafNode(tag="a", props={
            "href": "google.com"
        })

        self.assertRaises(ValueError, leaf_node.to_html)
    
    def test_no_tag(self):
        leaf_node = LeafNode(value="my raw text", props={
            "href": "google.com"
        })

        self.assertEqual("my raw text", leaf_node.to_html())

    def test_render_html(self):
        leaf_node = LeafNode(tag="a", value="My link", props={
            "href": "google.com"
        })

        self.assertEqual(
            "<a href='google.com'>My link</a>",
            leaf_node.to_html()
        )

if __name__ == "__main__":
    unittest.main()