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