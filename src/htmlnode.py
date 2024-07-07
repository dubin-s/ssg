class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        html = ""
        for k, v in self.props.items():
            html += (f' {k}="{v}"')
        return html

    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"
