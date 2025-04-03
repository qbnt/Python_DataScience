def NULL_not_found(object: any) -> int:
    oType = type(object)

    if isinstance(object, bool) and not object:
        print(f"Fake : {object} <class '{oType.__name__}'>")

    elif isinstance(object, float) and object != object:
        print(f"Cheese : {object} <class '{oType.__name__}'>")

    elif not object:
        match object:
            case None:
                print(f"Nothing : {object} <class '{oType.__name__}'>")
            case 0:
                print(f"Zero : {object} <class '{oType.__name__}'>")
            case "":
                print(f"Empty : {object} <class '{oType.__name__}'>")

    else:
        print("Type not Found")
        return 1

    return 0
