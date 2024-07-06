from textnode import TextNode, text_type_bold


def main():
    test = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
    print(test)


main()
