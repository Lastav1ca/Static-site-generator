import unittest

from inline_markdown import split_nodes_image, split_nodes_link, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestSplitImagesLinks(unittest.TestCase):
    def test_eq(self):
        node = TextNode(
            "Ovo je tekst sa linkom [za youtube](https://www.youtube.com) i [za facebook](https://www.facebook.com)",
            TextType.TEXT,
        )
        res = split_nodes_link([node])
        trazeni_res = [
            TextNode("Ovo je tekst sa linkom ", TextType.TEXT),
            TextNode("za youtube", TextType.LINK, "https://www.youtube.com"),
            TextNode(" i ", TextType.TEXT),
            TextNode("za facebook", TextType.LINK, "https://www.facebook.com"),
            ]
        self.assertEqual(res, trazeni_res)
