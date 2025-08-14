from textnode import TextNode


def main():
    node = TextNode()
    node.text = "Hello, World!"
    node.text_type = "bold"
    node.url = "http://example.com"

    print(node)


if __name__ == "__main__":
    main()
