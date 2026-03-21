class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        # String koji predstavlja ime HTML taga
        self.tag = tag
        # String koji predstavlja vrednost HTML taga
        self.value = value
        # Lista HTML objekata koji su deca ovog nodea
        self.children = children
        # Recnik koji predstavlja atribute HTML taga
        self.props = props

        #Ako su svi atributi none, to je samo raw text


    def to_html(self):
        raise NotImplemented
        
    def props_to_html(self):
        if not self.props:
            return ""
            
        res = ""
        for self.prop in self.props:
            res += f"{self.prop} = \"{self.props[self.prop]}\" "

        return res
        
    def __repr__(self):
        res = f'TAG: {self.tag}, VALUE: {self.value}, CHILDREN: {self.children}, PROPS: {self.props}'
    