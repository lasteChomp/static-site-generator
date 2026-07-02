def markdown_to_blocks(markdown: str) -> list[str]:
    markdown_split = markdown.split("\n\n")
    blocks = []
    for block in markdown_split:
        if block == "":
            continue
        blocks.append(block.strip())
    return blocks