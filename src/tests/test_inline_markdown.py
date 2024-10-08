import unittest
from src.inline_markdown import *
from src.textnode import *

class TextInlineMarkdown(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()