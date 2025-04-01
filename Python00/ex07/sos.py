import sys

NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}

ERR = "AssertionError: the arguments are bad"

def main():
    try:
        assert len(sys.argv) == 2, ERR
    except AssertionError as e:
        print(e)
        return 1
    str = sys.argv[1]
    res = ""
    for c in str:
        try:
            if c.isalnum() or c.isspace():
                print(c)
                m = str(NESTED_MORSE.get(c.upper()))
                res += m + " "
            else:
                raise AssertionError(ERR)
        except AssertionError as e:
            print(e)
            return 1
    print(res)
    return 0


if __name__ == "__main__":
    main()
