def shift_string(string, offset):
    if offset == 0:
        return string
    return string[offset:len(string)] + string[0:offset]
