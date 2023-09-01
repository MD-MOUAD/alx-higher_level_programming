#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    values = list(a_dictionary.values())
    big = values[0]
    for i in values:
        big = i if i > big else big
    return big
