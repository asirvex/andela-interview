def reverse_int_list(int_list):
    return int_list[::-1]

def upper_str_list(string_list):
    upper_list = []
    for string in string_list:
        upper_list.append(string.upper())
    return upper_list

def switch_reverse(items_list):
    integers = 0
    strings = 0
    for item in items_list:
        if type(item) == int:
            integers += 1
        elif type(item) == str:
            strings += 1

    if integers == len(items_list):
        return reverse_int_list(items_list)
    elif strings == len(items_list):
        return upper_str_list(items_list)
    else:
        return items_list
    