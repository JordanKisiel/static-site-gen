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

def split_nodes_link(old_nodes):
    # create a list for new nodes to return
    new_nodes = []

    for node in old_nodes:
        # if the node is already formatted
        # add it and do nothing else
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        #initialize orig text to the node's text
        orig_text = node.text

        #extract out link data
        extracted_links = extract_markdown_links(orig_text)
        #if there are no links, add the text as a single node
        #and do nothing else
        if len(extracted_links) == 0:
            new_nodes.append(node)
            continue

        #loop through all the extracted links
        for link in extracted_links:
            display_text = link[0]
            href = link[1]
            #use an interpolated delimiter to split one time
            #so that we're guaranteed to end up with two sections
            sections = orig_text.split(f"[{display_text}]({href})", 1)
            #if we don't end up with 2 sections, something went wrong
            if len(sections) != 2:
                raise ValueError("Invalid markdown: link section not closed")
            #if the first section is NOT an empty string
            #add it as a regular text node to new nodes
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            #in any case, append a link TextNode
            new_nodes.append(TextNode(display_text, text_type_link, href))
            #set orig text to second of the two sections that were created
            orig_text = sections[1]

        #after going through all the links,
        #if orig text is NOT an empty string
        #append the last bit of remaining text to new nodes
        if orig_text != "":
            new_nodes.append(TextNode(orig_text, text_type_text))

    return new_nodes

def split_nodes_image(old_nodes):
    #create a list for new nodes to return
    new_nodes = []

    for node in old_nodes:
        #if the node is already formatted
        #add it and do nothing else
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        
        #initialize orig text to the node's alt text 
        orig_text = node.text

        #extract out image data
        extracted_images = extract_markdown_images(orig_text)

        #if there are no images, add the text as a single node
        #and do nothing else
        if len(extracted_images) == 0:
            new_nodes.append(node) 
            continue

        #loop through all the extracted images
        for image in extracted_images:
            alt = image[0]
            src = image[1]

            #use an interpolated delimiter to split one time
            #so that we're guaranteed to end up with two sections
            sections = orig_text.split(f"![{alt}]({src})", 1)

            #if there are somehow not exactly 2 sections
            #something went wrong
            if len(sections) != 2:
                raise ValueError("Invalid markdown: image section not closed")
            #if the first section is NOT an empty string
            #add it as a regular text node to new nodes
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            #in any case, append an image TextNode
            new_nodes.append(TextNode(alt, text_type_image, src))
            #set orig text to the second of the two sections that were created
            orig_text = sections[1]

        #after going through all the images,
        #if orig text is NOT an empty string
        #append the last bit of remaining text to new nodes
        if orig_text != "":
            new_nodes.append(TextNode(orig_text, text_type_text))

    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

    

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def extract_images_and_links(text):
    return {
        "images": extract_markdown_images(text),
        "links": extract_markdown_links(text)
    }