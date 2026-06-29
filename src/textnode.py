from enum import Enum

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