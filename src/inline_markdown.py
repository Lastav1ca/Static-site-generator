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


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:

        alts_and_urls = extract_markdown_links(node.text)

        original_text = node.text

        for alt,url in alts_and_urls:

            sections = original_text.split(f"[{alt}]({url})", 1)
            #sada je sections[0] tekst pre linka
            #sections[1] je tekst nakon linka

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(
                alt,
                TextType.LINK,
                url
            ))

            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:

        alts_and_imgs = extract_markdown_links(node.text)

        original_text = node.text

        for alt,img in alts_and_imgs:

            sections = original_text.split(f"[{alt}]({img})", 1)
            #sada je sections[0] tekst pre slike
            #sections[1] je tekst nakon slike

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(
                alt,
                TextType.LINK,
                img
            ))

            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes
