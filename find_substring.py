from collections import Counter

def find_substrings(grammar):
    """
    Finds all repeating subsequences of length >= 2) in the right side of bthe grammar.(but it counts overlapping sequence)
    """
    # A Counter acts like a dictionary that automatically defaults to 0
    substring_counts = Counter()
    # Iterate through the lists of tokens for every rule in the grammar

    for rule_name, token_list in grammar.items():
        n = len(token_list)
        # Extract all possible substrings of length 2 up to the length of the rule
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                # Slice the list to get the substring
                sub_list = token_list[i: i + length]
                # Convert to a tuple , it is necessary to be counted
                candidate = tuple(sub_list)
                # Add to our global count
                substring_counts[candidate] += 1

    # Filter and return only the candidates that appear 2 or more times in total.
    # We do not care if they overlap at this stage; we just need them to exist.
    valid_candidates = [sub for sub, count in substring_counts.items() if count >= 2]

    return valid_candidates

