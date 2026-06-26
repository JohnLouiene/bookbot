#Returns the number of words inside a string
def get_num_words(string):
    return len(string.split())

#Takes a string and returns a dictionary of string -> integer
#Where string is a character and integer is the number of times the character appears
def get_ch_dict(string):
    string_lower = string.lower()
    ch_count = {}
    for ch in string_lower:
        if ch not in ch_count:
            ch_count[ch] = 1
        else:
            ch_count[ch] += 1
    return ch_count

#Takes a dictionary and returns a sorted list
def sort_dict(dictionary):
    sorted_list = list()
    for ch in dictionary:
        num = dictionary[ch]
        sorted_list.append([ch, num])

    sorted_list.sort(key=lambda x:x[1], reverse=True)
    return sorted_list

def sort_on(list_to_sort: tuple[str, int]) -> int:
    return list_to_sort[1]

def chars_dict_to_sorted_list(sorted_dict: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list = []

    for key in sorted_dict.keys():
        sorted_list.append((key, sorted_dict[key]))

    sorted_list = sorted(sorted_list, key=sort_on, reverse=True)

    return sorted_list
    