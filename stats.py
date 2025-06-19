def get_word_count(contents):
    words = contents.split()
    return len(words)

def get_char_counts(content):
    char_counts = {}
    for char in content:
        char_low = char.lower()
        if char_low in char_counts:
            char_counts[char_low] += 1
        else:
            char_counts[char_low] = 1
    return char_counts


def get_sorted_list(unsorted_dict):
    list_of_dicts = []
    for d in unsorted_dict:
        list_of_dicts.append({
            "char": d,
            "num": unsorted_dict[d]
         })
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts


def sort_on(d):
    return d["num"]
