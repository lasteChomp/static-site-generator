from textnode import TextNode, TextType


def main():
    textnode = TextNode("I will get hired", TextType.LINK, "https://www.boot.dev")
    print(textnode)

main()