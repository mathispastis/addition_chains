from non_overlapping_counter import count_non_overlapping
from replace_token import replace_tokens
from find_substring import find_substrings


def greedy_complete(input_sequence):
    """
    Greedy algorithm computes the grammar "until the end"
    """
    grammar = {'A0': list(input_sequence)}
    rule_counter = 1

    while True:
        # Find all repeating substrings (length >= 2)
        candidates = find_substrings(grammar)

        if not candidates:
            break

        best_substring = None
        max_savings = -1

        # calculate the saving: (L - 1)k - L
        for sub in candidates:
            L = len(sub)
            k = count_non_overlapping(grammar, sub)
            current_savings = (L - 1) * k - L

            # here it follows the rule: we take the first
            if current_savings > max_savings:
                max_savings = current_savings
                best_substring = sub

        if max_savings < 0 or best_substring is None:
            break

        new_rule_name = f'A{rule_counter}'

        grammar[new_rule_name] = list(best_substring)

        replace_tokens(grammar, best_substring, new_rule_name)

        rule_counter += 1

    return grammar
