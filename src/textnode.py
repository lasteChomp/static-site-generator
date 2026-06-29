from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    PLAIN_TEXT = "text"
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return (
            self.text == other.text and self.text_type == other.text_type and self.url == other.url
        )

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("LINK type requires a url")
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("IMAGE type requires a url")
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError("invalid text type")