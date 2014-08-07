def shift_string(string, offset):
    if offset == 0:
        return string
    return string[offset:len(string)] + string[0:offset]

def crack_sort(l):
    return sorted(l, key=lambda x: -1 if "MCA-" in x else 0)
