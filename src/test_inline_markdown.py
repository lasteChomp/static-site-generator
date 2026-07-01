import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestInlineMarkdown(unittest.TestCase):
    def test_split_delimeter_plain_text(self):
        node1 = TextNode("This is a plain text", TextType.PLAIN_TEXT)
        node2 = TextNode("This is another plain text", TextType.PLAIN_TEXT)
        node3 = TextNode("This is also another plain text", TextType.PLAIN_TEXT)
        nodes = [node1, node2, node3]
        nodes_splitted = split_nodes_delimiter(nodes, "_", TextType.PLAIN_TEXT)
        self.assertEqual(nodes, nodes_splitted)

    def test_split_delimeter_bold_single_node(self):
        node = TextNode("This is a text with a **bold** word.", TextType.PLAIN_TEXT)
        nodes = [node]
        compare_against = [
            TextNode("This is a text with a ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" word.", TextType.PLAIN_TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, compare_against)

    def test_split_delimeter_bold_multiple_nodes(self):
        node = TextNode("This is a text with a **bold** word.", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a **text** with a **bold** word.", TextType.PLAIN_TEXT)
        nodes = [node, node2]
        compare_against = [
            TextNode("This is a text with a ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" word.", TextType.PLAIN_TEXT),
            TextNode("This is a ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with a ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" word.", TextType.PLAIN_TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, compare_against)

    def test_split_delimeter_italic_single_node(self):
        node = TextNode("This is a text with a _italic_ word.", TextType.PLAIN_TEXT)
        nodes = [node]
        compare_against = [
            TextNode("This is a text with a ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word.", TextType.PLAIN_TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, compare_against)

    def test_split_delimeter_italic_multiple_nodes(self):
        node = TextNode("This is a text with a _italic_ word.", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a _text_ with a _italic_ word.", TextType.PLAIN_TEXT)
        nodes = [node, node2]
        compare_against = [
            TextNode("This is a text with a ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word.", TextType.PLAIN_TEXT),
            TextNode("This is a ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.ITALIC_TEXT),
            TextNode(" with a ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word.", TextType.PLAIN_TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, compare_against)

    def test_split_delimeter_code_single_node(self):
        node = TextNode("This is a text with a `code block` word.", TextType.PLAIN_TEXT)
        nodes = [node]
        compare_against = [
            TextNode("This is a text with a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word.", TextType.PLAIN_TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, compare_against)

    def test_split_delimeter_code_multiple_nodes(self):
        node = TextNode("This is a text with a `code block` word.", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a `text` with a `code block` word.", TextType.PLAIN_TEXT)
        nodes = [node, node2]
        compare_against = [
            TextNode("This is a text with a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word.", TextType.PLAIN_TEXT),
            TextNode("This is a ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.CODE),
            TextNode(" with a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word.", TextType.PLAIN_TEXT)
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, compare_against)

    def test_split_delimeter_multiple_types_node(self):
        node = TextNode("This is **bold** and _italic_ and `code` together", TextType.PLAIN_TEXT)
        nodes = [node]
        compare_against = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" together", TextType.PLAIN_TEXT)
        ]
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(nodes, compare_against)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ], matches)