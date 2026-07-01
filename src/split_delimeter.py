from textnode import TextNode, TextType

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
        
        