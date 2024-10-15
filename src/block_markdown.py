import re
from src.htmlnode import * 
from src.inline_markdown import * 

block_type_paragraph= "paragraph"
block_type_heading = "heading"
block_type_quote = "quote"
block_type_code = "code"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

def markdown_to_block(markdown):
    # create list of blocks to return
    resulting_blocks = []
    # split markdown using newlines as delimiter
    blocks = re.split(r"\n\s*\n", markdown)

    # loop through each block item
    for block in blocks:
        # strip off any whitespace from the beginning
        # or end
        resulting_block = block.strip()

        # remove any empty block items
        if resulting_block != "":
            resulting_blocks.append(resulting_block)

    return resulting_blocks

def block_to_block_type(md_block):
    heading_match = re.fullmatch(r"#{1,6}[ ].*", md_block)
    if heading_match != None:
        return block_type_heading
    
    code_match = re.fullmatch(r"`{3}(.|\n)*`{3}", md_block)
    if code_match != None:
        return block_type_code
    
    lines = md_block.split("\n")
    quote_matches = []
    for line in lines:
        line_match= re.fullmatch(r">.*", line)
        if line_match != None:
            quote_matches.append(line_match)
    if len(quote_matches) == len(lines):
        return block_type_quote
    
    unordered_matches = []
    for line in lines:
        line_match = re.fullmatch(r"[*-][ ].*", line)
        if line_match != None:
            unordered_matches.append(line_match)
    if len(unordered_matches) == len(lines):
        return block_type_unordered_list
    
    ordered_matches = []
    for line in lines:
        line_match = re.fullmatch(r"\d[.][ ].*", line)
        if line_match != None:
            ordered_matches.append(line_match)
    if len(ordered_matches) == len(lines):
        return block_type_ordered_list
    
    return block_type_paragraph


def markdown_to_html_node(markdown):
    # split the markdown into blocks
    blocks = markdown_to_block(markdown)
    
    # create an empty list for any children
    children = []

    # loop over each block created above
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    return ParentNode("div", children, None)

    
def block_to_html_node(block):
    type = block_to_block_type(block)

    if type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if type == block_type_code:
        return code_to_html_node(block)
    if type == block_type_heading:
        return heading_to_html_node(block)
    if type == block_type_ordered_list:
        return olist_to_html_node(block)
    if type == block_type_unordered_list:
        return ulist_to_html_node(block)
    if type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    heading_parts = block.split(" ", 1)
    level = len(heading_parts[0])
    value = heading_parts[1]

    if level < 1 or level > 6:
        raise ValueError("Heading levels must be between 1-6, inclusive")
    
    children = text_to_children(value)

    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    value = block[4:-3]
    children = text_to_children(value)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def extract_title(markdown):
    blocks = markdown_to_block(markdown)

    for block in blocks:
        heading_match = re.fullmatch(r"#{1}[ ].*", block)
        if heading_match != None:
            return block[2:].strip()
        
    raise Exception("Document needs at least one h1 header")