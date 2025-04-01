import sys
import string


class lexeur:
    def __init__(self, txt):
        self.txt = txt

    def charNb(self):
        return len(self.txt)

    def upperNb(self):
        return sum(1 for c in self.txt if c.isupper())

    def lowerNb(self):
        return sum(1 for c in self.txt if c.islower())

    def punctNb(self):
        return sum(1 for c in self.txt if c in string.punctuation)

    def spaceNb(self):
        return sum(1 for c in self.txt if c.isspace())

    def digitNb(self):
        return sum(1 for c in self.txt if c.isdigit())


def main():
    try:
        assert len(sys.argv) <= 2, "Too many arguments"
    except AssertionError as e:
        print(e)
        return 1

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        text = input()

    lex = lexeur(text)

    print(f"The text contains {lex.charNb()} characters:")
    print(f"{lex.upperNb()} upper letters")
    print(f"{lex.lowerNb()} lower letters")
    print(f"{lex.punctNb()} punctuation marks")
    print(f"{lex.spaceNb()} spaces")
    print(f"{lex.digitNb()} digits")

    return 0


if __name__ == "__main__":
    main()
