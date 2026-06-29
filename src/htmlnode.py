class HTMLNode:
    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list["HTMLNode"] | None = None, 
            props: dict[str, str] | None = None
            ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("Child classes must override this method")
    
    def props_to_html(self) -> str:
        if self.props is None or len(self.props) == 0:
            return ""
        
        formatted_str = ""
        for key, value in self.props.items():
            prop = f' {key}="{value}"'
            formatted_str += prop

        return formatted_str
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}(tag='{self.tag}', value='{self.value}', children='{self.children}', props='{self.props_to_html()}')"
    

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None , value: str , props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, children=None, props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}(tag='{self.tag}', value='{self.value}', props='{self.props_to_html()}')"