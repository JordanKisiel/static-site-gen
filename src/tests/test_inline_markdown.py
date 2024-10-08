import unittest
from src.inline_markdown import *
from src.textnode import *

class TestInlineMarkdown(unittest.TestCase):
    def test_bold(self):
        node = TextNode("text with **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("text with ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes
        )

    def test_double_bold(self):
        node = TextNode("text with **two** **bolded words**!", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)

        self.assertListEqual(
            [
                TextNode("text with ", text_type_text),
                TextNode("two", text_type_bold),
                TextNode(" ", text_type_text),
                TextNode("bolded words", text_type_bold),
                TextNode("!", text_type_text)
            ],
            new_nodes
        )

    def test_italic(self):
        node = TextNode("text with *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("text with ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes
        )

    def test_bold_and_italic(self):
        node = TextNode("text with **bold** and *italic* words", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)

        self.assertListEqual(
            [
                TextNode("text with ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" words", text_type_text),
            ],
            new_nodes
        )

    def test_code(self):
        node = TextNode("text with `code block`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("text with ", text_type_text),
                TextNode("code block", text_type_code),
            ],
            new_nodes
        )

    def test_format_error(self):
        node = TextNode("text with format **error oops", text_type_text)

        self.assertRaises(ValueError, split_nodes_delimiter, [node], "**", text_type_bold)

    def test_extract_images_and_links(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

        self.assertEqual(
            extract_images_and_links(text)["images"],
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        )

        self.assertEqual(
            extract_images_and_links(text)["links"],
            [] 
        )

        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        self.assertEqual(
            extract_images_and_links(text2)["images"],
            []
        )

        self.assertEqual(
            extract_images_and_links(text2)["links"],
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        )


        text3 = "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        self.assertEqual(
            extract_images_and_links(text3)["images"],
            [("to boot dev", "https://www.boot.dev")]
        )

        self.assertEqual(
            extract_images_and_links(text3)["links"],
            [("to youtube", "https://www.youtube.com/@bootdotdev")]
        )
 

if __name__ == "__main__":
    unittest.main()