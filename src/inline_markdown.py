from textnode import TextNode, TextType
from re import findall

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        nodes_splitted = []
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid markdown, formatted section not closed: {delimiter}")
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                nodes_splitted.append(TextNode(part, TextType.PLAIN_TEXT))
            else:
                nodes_splitted.append(TextNode(part, text_type))
        new_nodes.extend(nodes_splitted)
    return new_nodes
        
def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        extracted_markdown_image = extract_markdown_images(node.text)
        if len(extracted_markdown_image) == 0:
            new_nodes.append(node)
            continue
        for image in extracted_markdown_image:
            image_alt = image[0]
            image_url = image[1]
            parts = node.text.split(f"![{image_alt}]({image_url})", maxsplit=1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
            node.text = parts[1]
        if node.text != "":
            new_nodes.append(TextNode(node.text, TextType.PLAIN_TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        extracted_markdown_link = extract_markdown_links(node.text)
        if len(extracted_markdown_link) == 0:
            new_nodes.append(node)
            continue
        for link in extracted_markdown_link:
            link_alt = link[0]
            link_url = link[1]
            parts = node.text.split(f"[{link_alt}]({link_url})", maxsplit=1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            node.text = parts[1]
        if node.text != "":
            new_nodes.append(TextNode(node.text, TextType.PLAIN_TEXT))
    return new_nodes

            