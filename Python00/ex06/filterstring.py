from ft_filter import ft_filter
import sys


ERR = "AssertionError: the arguments are bad"


def main():
    try:
        assert len(sys.argv) == 3, ERR
        str = sys.argv[1]
        assert len(str) > 0, ERR
        nb = sys.argv[2]
        assert nb.isdigit(), ERR
    except AssertionError as e:
        print(e)
        return 1

    intNb = int(nb)
    res = list(ft_filter(lambda x: len(x) > intNb, str.split()))
    print(res)
    return 0


if __name__ == "__main__":
    main()
