def NULL_not_found(object: any) -> int:
    det = str(type(object))

    if (object is None):
        print("Nothing:", object, det)
    elif (type(object) is float and float(object) != float(object)):
        print("Chesse:", float(object), det)
    elif (type(object) is int and object == 0):
        print("Zero:", int(object), det)
    elif (type(object) is str and len(object) == 0):
        print("Empty:", (object), det)
    elif (type(object) is bool and object == False):
        print("Fake:", (object), det)
    else:
        print("Type not Found")
        return 1
    return 0

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
