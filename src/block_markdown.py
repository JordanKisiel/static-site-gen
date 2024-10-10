import re

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
