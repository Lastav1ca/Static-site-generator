from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if delimiter not in node.text:
            raise ValueError("Delimiter nije pronađen u stringu")
        
        node_text = node.text.split(delimiter)

        new_node = []

        new_node.append(TextNode(node_text[0], TextType.TEXT))
        new_node.append(TextNode(node_text[1], TextType.CODE))
        new_node.append(TextNode(node_text[2], TextType.TEXT))

        new_nodes.extend(new_node)

    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
