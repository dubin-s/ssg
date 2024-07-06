import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("testing node", "italic", "https://www.google.com")
        node2 = TextNode("testing node", "bold", "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_nourl(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()