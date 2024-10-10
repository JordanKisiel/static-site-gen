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

if __name__ == "__main__":
    unittest.main()