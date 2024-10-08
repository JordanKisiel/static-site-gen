import unittest
from src.textnode import * 

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "italic", "something.com")
        node2 = TextNode("This is a text node", "italic", "something.com")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text nod", "italic", "something.com")
        node2 = TextNode("This is a text node", "italic", "something.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", "bold", "something.com")
        node2 = TextNode("This is a text node", "italic", "something.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "italic", "somethingcom")
        node2 = TextNode("This is a text node", "italic", "something.com")
        self.assertNotEqual(node, node2)

    def test_text_to_html(self):
        text_node = TextNode("raw text", text_type_text)

        self.assertEqual(text_node_to_html_node(text_node).value, "raw text")
        self.assertEqual(text_node_to_html_node(text_node).tag, None)

    def test_bold_to_html(self):
        bold_node = TextNode("bold text", text_type_bold)

        self.assertEqual(text_node_to_html_node(bold_node).value, "bold text")
        self.assertEqual(text_node_to_html_node(bold_node).tag, "b")

 
    def test_italic_to_html(self):
        italic_node = TextNode("italic text", text_type_italic)

        self.assertEqual(text_node_to_html_node(italic_node).value, "italic text")   
        self.assertEqual(text_node_to_html_node(italic_node).tag, "i")   

    def test_code_to_html(self):
        code_node = TextNode("code text", text_type_code)

        self.assertEqual(text_node_to_html_node(code_node).value, "code text")
        self.assertEqual(text_node_to_html_node(code_node).tag, "code")

    def test_link_to_html(self):
        link_node = TextNode("link text", text_type_link, "google.com")

        self.assertEqual(text_node_to_html_node(link_node).value, "link text")
        self.assertEqual(text_node_to_html_node(link_node).tag, "a")
        self.assertEqual(text_node_to_html_node(link_node).props["href"], "google.com")

    def test_image_to_html(self):
        image_node = TextNode("image alt text", text_type_image, "/path/to/image.jpg")

        self.assertEqual(text_node_to_html_node(image_node).tag, "img")
        self.assertEqual(text_node_to_html_node(image_node).props["src"], "/path/to/image.jpg")
        self.assertEqual(text_node_to_html_node(image_node).props["alt"], "image alt text")

    def test_text_type_error(self):
        text_node = TextNode("raw text", "invalid text type")

        self.assertRaises(Exception, text_node_to_html_node, text_node) 

if __name__ == "__main__":
    unittest.main()