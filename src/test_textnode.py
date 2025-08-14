import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node3, node4)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        node_with_url = TextNode("This is a link", TextType.LINK, url="http://example.com")
        html_node_with_url = text_node_to_html_node(node_with_url)
        self.assertEqual(html_node_with_url.tag, "a")
        self.assertEqual(html_node_with_url.value, "This is a link")
        self.assertEqual(html_node_with_url.props, {"href": "http://example.com"})

        node_with_image = TextNode("This is an image", TextType.IMAGE, url="http://example.com/image.png")
        html_node_with_image = text_node_to_html_node(node_with_image)
        self.assertEqual(html_node_with_image.tag, "img")
        self.assertEqual(html_node_with_image.props, {"src": "http://example.com/image.png", "alt": "This is an image"})


if __name__ == "__main__":
    unittest.main()
