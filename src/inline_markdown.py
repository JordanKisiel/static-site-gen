from src.textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # create a list for the new nodes
    new_nodes = []
    # iterate through each node in old nodes
    for node in old_nodes:
        # if the node is not a regular text node (already
        # formatted) then simply add it to the new nodes list
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        # otherwise split the text in the text node using delimiters 
        split_text = node.text.split(delimiter)
        
        # if the number of text items is even,
        # the original markdown text was not formatted correctly
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        # otherwise, loop through each split text item
        # adding different TextNodes to the new list
        # depending on whether the index is even or odd
        for i in range(0, len(split_text)):
            if split_text[i] == "":
                # disregard empty strings
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], text_type_text))
            else:
                new_nodes.append(TextNode(split_text[i], text_type))
    
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)

def extract_images_and_links(text):
    return {
        "images": extract_markdown_images(text),
        "links": extract_markdown_links(text)
    }