import unittest
from src.block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_block_markdown(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ],
            markdown_to_block(text)
        )

        text2 = """This is the first line
        
        This is the second line

        
        This line has an excessive new line above it        
        """

        self.assertListEqual(
            [
                "This is the first line",
                "This is the second line",
                "This line has an excessive new line above it"
            ],
            markdown_to_block(text2)
        )

    def test_block_to_block_type(self):
        heading_block1 = "# This is a heading"
        heading_block2 = "###### This is a heading too"
        heading_block3 = "####### This is NOT a heading"
        heading_block4 = "#*# This is also NOT a heading"

        self.assertEqual(
            block_to_block_type(heading_block1),
            block_type_heading
        )

        self.assertEqual(
            block_to_block_type(heading_block2),
            block_type_heading
        )

        self.assertNotEqual(
            block_to_block_type(heading_block3),
            block_type_heading
        )

        self.assertNotEqual(
            block_to_block_type(heading_block4),
            block_type_heading
        )

        code_block1 = "```This is a single line code block```"
        code_block2 = "```This is a multiline\nCode block\nYep```"
        code_block3 = "```This is not a code block"
        code_block4 = "This is also not a code block```"
        code_block5 = "```This is also not a ```code block"

        self.assertEqual(
            block_to_block_type(code_block1),
            block_type_code
        )

        self.assertEqual(
            block_to_block_type(code_block2),
            block_type_code
        )

        self.assertNotEqual(
            block_to_block_type(code_block3),
            block_type_code
        )

        self.assertNotEqual(
            block_to_block_type(code_block4),
            block_type_code
        )

        self.assertNotEqual(
            block_to_block_type(code_block5),
            block_type_code
        )

        quote_block1 = ">This is a quote block\n> Yes indeed\n>it sure is"
        quote_block2 = ">This is NOT a quote block\nNope indeed\n>it sure isn't"
        quote_block3 = "This is NOT a quote block\n>Nope indeed\n>it sure isn't"
        quote_block4 = ">This is NOT a quote block\n>Nope indeed\nit sure isn't"

        self.assertEqual(
            block_to_block_type(quote_block1),
            block_type_quote
        )

        self.assertNotEqual(
            block_to_block_type(quote_block2),
            block_type_quote
        ) 
        
        self.assertNotEqual(
            block_to_block_type(quote_block3),
            block_type_quote
        ) 

        self.assertNotEqual(
            block_to_block_type(quote_block4),
            block_type_quote
        )

        unordered_block1 = "* This is an ul block\n- Yep it sure is\n* Yep"
        unordered_block2 = " This is NOT an ul block\n- Yep it sure is\n* Yep"
        unordered_block3 = "*This is NOT an ul block\n- Yep it sure is\n* Yep"
        unordered_block4 = "* This is NOT an ul block\n+ Yep it sure is\n* Yep"

        self.assertEqual(
            block_to_block_type(unordered_block1),
            block_type_unordered_list
        )

        self.assertNotEqual(
            block_to_block_type(unordered_block2),
            block_type_unordered_list
        ) 
        
        self.assertNotEqual(
            block_to_block_type(unordered_block3),
            block_type_unordered_list
        ) 

        self.assertNotEqual(
            block_to_block_type(unordered_block4),
            block_type_unordered_list
        )

        ordered_block1 = "1. this is an\n2. list\n3. Yep"
        ordered_block2 = "1.this is NOT an\n2. list\n3. Yep"
        ordered_block3 = "1. this is NOT an\n2 list\n3. Yep"
        ordered_block4 = "1. this is NOT an\n2. list\na. Yep"

        self.assertEqual(
            block_to_block_type(ordered_block1),
            block_type_ordered_list
        )

        self.assertNotEqual(
            block_to_block_type(ordered_block2),
            block_type_ordered_list
        ) 
        
        self.assertNotEqual(
            block_to_block_type(ordered_block3),
            block_type_ordered_list
        ) 

        self.assertNotEqual(
            block_to_block_type(ordered_block4),
            block_type_ordered_list
        )

        para_block = "This is a just a regular\nparagraph\nYep"

        self.assertEqual(
            block_to_block_type(para_block),
            block_type_paragraph
        )
    
    def test_paragraph(self):
        md = """
This is a **bolded** paragraph
text in a p
tag here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This is a <b>bolded</b> paragraph text in a p tag here</p></div>"
        )

    def test_paragraphs(self):
        md = """
This is a **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This is a <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        )
        
    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>"
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""
        
        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>"
        )

    def test_extract_title(self):
        md = """
This is not a title

#  This is a title  

This is also not a title

"""

        self.assertEqual(
            extract_title(md),
            "This is a title"
        )





if __name__ == "__main__":
    unittest.main()