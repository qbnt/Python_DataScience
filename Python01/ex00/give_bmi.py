ERR_SIZE = "Error: Height and weight haven't the same size"


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    try:
        assert height and weight and len(height) == len(weight), ERR_SIZE
    except AssertionError as e:
        print(e)
        exit(1)

    bmi = []
    for h, w in zip(height, weight):
        bmi.append(w / (h ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = []
    for i in bmi:
        res.append(i >= limit)

    return res
