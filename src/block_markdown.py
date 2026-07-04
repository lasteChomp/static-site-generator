from enum import Enum
from htmlnode import ParentNode, HTMLNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    markdown_split = markdown.split("\n\n")
    blocks = []
    for block in markdown_split:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks

def block_to_block_type(block: str) -> BlockType:
    if block.startswith("#") and "# " in block:
        count = 0
        for char in block:
            if char == "#":
                count += 1
            else:
                break
        if count >= 1 and count <= 6:
            return BlockType.HEADING
        return BlockType.PARAGRAPH
    if block.startswith("```\n") and block.endswith("\n```"):
        return BlockType.CODE
    if block.startswith(">"):
        if "\n" not in block:
            return BlockType.QUOTE
        lines = block.splitlines()
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE    
    if block.startswith("- "):
        if "\n" not in block:
            return BlockType.UNORDERED_LIST
        lines = block.splitlines()
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        if "\n" not in block:
            return BlockType.ORDERED_LIST
        lines = block.splitlines()
        order_num = 1
        for line in lines:
            if not line.startswith(f"{order_num}. "):
                return BlockType.PARAGRAPH
            order_num += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(block: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(block)
    children = []
    for text_node in text_nodes:
        leaf_nodes = text_node_to_html_node(text_node)
        children.append(leaf_nodes)
    return children

def block_to_parent_node(block: str) -> ParentNode:
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.HEADING:
            heading_size = block.count("#")
            block = block[heading_size + 1:]
            children = text_to_children(block)
            return ParentNode(tag= f"h{heading_size}", children=children)
        case BlockType.CODE:
            block = block[4:-3]
            text_node = TextNode(text=block, text_type=TextType.CODE)
            leaf_node = text_node_to_html_node(text_node)
            return ParentNode(tag="pre", children=[leaf_node])
        case BlockType.QUOTE:
            block = block.replace("> ", "").replace(">", "").replace("\n", " ")
            children = text_to_children(block)
            quote_p = ParentNode(tag="p", children=children)
            return ParentNode(tag="blockquote", children=[quote_p])
        case BlockType.UNORDERED_LIST:
            block = block.replace("- ", "")
            lines = block.splitlines()
            ul_items = []
            for line in lines:
                children = text_to_children(line)
                ul_item = ParentNode(tag="li", children=children)
                ul_items.append(ul_item)
            return ParentNode(tag="ul", children=ul_items)
        case BlockType.ORDERED_LIST:
            lines = block.splitlines()
            ol_items = []
            for line in lines:
                line = line[3:]
                children = text_to_children(line)
                ol_item = ParentNode(tag="li", children=children)
                ol_items.append(ol_item)
            return ParentNode(tag="ol", children=ol_items)
        case _:
            if "\n" in block:
                block = block.replace("\n", " ")
            children = text_to_children(block)
            return ParentNode(tag="p", children=children)

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    blocks_nodes = []
    for block in blocks:
        parent_node = block_to_parent_node(block)
        blocks_nodes.append(parent_node)
    return ParentNode(tag="div", children=blocks_nodes)
    