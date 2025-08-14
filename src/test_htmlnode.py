import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="div", value=None, children=None, props={"class": "test", "id": "123"})
        self.assertEqual(node.props_to_html(), 'class="test" id="123"')

        node_empty = HTMLNode(tag="span", value=None, children=None, props={})
        self.assertEqual(node_empty.props_to_html(), "")

        node2 = HTMLNode(tag="a", value=None, children=None, props={"href": "http://example.com", "target": "_blank"})
        self.assertEqual(node2.props_to_html(), 'href="http://example.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=None, props={"class": "test"})
        self.assertEqual(repr(node), "HTMLNode('div', 'Hello', None, {'class': 'test'})")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node_with_props = LeafNode("p", "Hello, world!", props={"class": "greeting"})
        self.assertEqual(node_with_props.to_html(), '<p class="greeting">Hello, world!</p>')

        node_without_value = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node_without_value.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
