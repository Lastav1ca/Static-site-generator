from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError
        
        if not self.children:
            raise ValueError
        
        res = f"<{self.tag}>"

        for child in self.children:
            res += child.to_html()

        res += f"</{self.tag}>"

        return res
        
    