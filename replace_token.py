
def replace_tokens(grammar, best_substring, new_rule_name):
    """
    Replaces all non-overlapping occurrences of the best_substring
    with the new rule name across all rules in the grammar.
    """
    sub_len = len(best_substring)
    # We iterate through every rule in the grammar
    for rule_name, token_list in grammar.items():
        new_token_list = []  # We will build the updated rule here
        i = 0
        n = len(token_list)

        while i < n:
            # 1. Check if we have enough tokens left to make a match
            # 2. Check if the current window perfectly matches our substring
            if i <= n - sub_len and tuple(token_list[i: i + sub_len]) == best_substring:
                # their is a match so we add the new token instead of the old ones.
                new_token_list.append(new_rule_name)
                i += sub_len
            else:
                # No match. Just keep the original token and move forward by 1.
                new_token_list.append(token_list[i])
                i += 1

        # Overwrite the old rule
        grammar[rule_name] = new_token_list
    # add the new rule
    grammar[new_rule_name] = list(best_substring)
