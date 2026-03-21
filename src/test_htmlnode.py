import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_props(self):
        dict1 = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode('b', 'nesto', ['drugi', 'taj'], dict1)
        node1 = HTMLNode('b', 'nesto', ['drugi', 'taj'], dict1)

        props = node.props_to_html
        props1 = node.props_to_html
        self.assertEqual(props, props1)

    def test_eq_props_one_empty(self):
        dict1 = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode('b', 'nesto', ['drugi', 'taj'], dict1)
        node1 = HTMLNode('b', 'nesto', ['drugi', 'taj'])

        props = node.props_to_html
        props1 = node.props_to_html
        self.assertEqual(props, props1)

    def test_eq_props_both_empty(self):
        dict1 = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode()
        node1 = HTMLNode()

        props = node.props_to_html
        props1 = node.props_to_html
        self.assertEqual(props, props1)