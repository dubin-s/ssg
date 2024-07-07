import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "hello-div", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="hello-div" href="https://boot.dev"',
        )

if __name__ == "__main__":
    unittest.main()