from enum import Enum

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
    