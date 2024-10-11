import re
from src.htmlnode import HTMLNode 

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
        # string off any whitespace from the beginning
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

    # loop over each block created above
    for block in blocks:
        type = block_to_block_type(block)
        tag = block_type_to_tag(type, block)
        # value = get_value_from_block(block)
        node = HTMLNode(tag)

    # 1. determine the type of block using the block_to_block_type fn
    # 2. based on the type of block, create a new HTMLNode with the proper data
    # 3. Assign the proper child HTMLNode objects to the block node
    #     create a shared text_to_children(text) fn that works for all block types
    #        takes str, returns list of HTMLNodes that represent the inline markdown
    #        using previously created fn's (think TextNode -> HTMLNode)


    # Make all the block nodes children under a single parent HTML node (a div)
    # and return it
    

def block_type_to_tag(type, block):
    if type == block_type_paragraph: return "p"
    if type == block_type_quote: return "quote"
    if type == block_type_code: return "code"
    if type == block_type_unordered_list: return "ul" 
    if type == block_type_ordered_list: return "ol" 

    if type == block_type_heading:
        hashtags = block.split(" ", 1)[0]
        num_hashtags = len(hashtags)
        return f"h{num_hashtags}"
    
    raise ValueError("Invalid block type")

def get_value_from_block(block):
    #TODO
    pass