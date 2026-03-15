from find_substring import find_substrings

def count_non_overlapping(grammar, substring):
    """
    find k , the total number of non-overlapping
    occurrences of a substring in the grammar.
    it should replace the occurence from left to right like described in the paper
    """
    k = 0
    sub_len = len(substring)
     # Iterate through the lists of tokens for every rule in the grammar
    for rule_name, token_list in grammar.items():
        n = len(token_list)
        i = 0  # index
        # Slide through the list until we don't have enough room for the substring
        while i <= n - sub_len:
            # Slice the current window and compare it to our candidate tuple
            if tuple(token_list[i: i + sub_len]) == substring:
                k += 1
                i += sub_len
            else:
                i += 1
    return k



#def test_count_non_overlapping():
    grammar ={
        'A0': ['A0', 'A0', 'A0', 'a', 'b', 'a', 'a', 'b', 'a','b'],
        'A1': ['b', 'a', 'b']
    }
    k = count_non_overlapping(grammar, ('b', 'a'))
    print(k)
#test_count_non_overlapping()