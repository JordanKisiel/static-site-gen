import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_multiple_children(self):
        node = ParentNode(
            "p", 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
        )

        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html()
        )

    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(
                            "b",
                            "bold text",
                        ),
                        LeafNode(
                            "i",
                            "italic text"
                        )
                    ]
                ),
                LeafNode(
                    "a",
                    "link text",
                    {
                        "href": "google.com"
                    }
                )
            ]
        )
        
        self.assertEqual(
            "<p><p><b>bold text</b><i>italic text</i></p><a href='google.com'>link text</a></p>",
            node.to_html()
        )

    def test_children_is_none_error(self):
        node = ParentNode(
            "a",
            None,
            {
                "href": "google.com"
            }
        )

        self.assertRaises(ValueError, node.to_html)

    def test_no_children_error(self):
        node = ParentNode(
            "p",
            [],
        )

        self.assertRaises(ValueError, node.to_html)