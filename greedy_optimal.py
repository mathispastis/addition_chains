import copy
from non_overlapping_counter import count_non_overlapping
from replace_token import replace_tokens
from find_substring import find_substrings
import copy


def greedy_branching(grammar, rule_counter=1):
    """
    Recursively explores ALL paths when there is a tie in max_savings.
    """
    candidates = find_substrings(grammar)

    if not candidates:
        return [grammar]

    best_candidates = []
    max_savings = 0

    for sub in candidates:
        L = len(sub)
        k = count_non_overlapping(grammar, sub)
        current_savings = (L - 1) * k - L

        if current_savings > max_savings:
            max_savings = current_savings
            best_candidates = [sub]  # reset the tie list
        elif current_savings == max_savings and current_savings > 0:
            best_candidates.append(sub)  # add a tie

    if max_savings <= 0 or not best_candidates:
        return [grammar]

    all_final_grammars = []
    new_rule_name = f'A{rule_counter}'

    for best_sub in best_candidates:
        # Clone the grammar
        branched_grammar = copy.deepcopy(grammar)

        # Apply the replacement for this specific branch
        replace_tokens(branched_grammar, best_sub, new_rule_name)
        branched_grammar[new_rule_name] = list(best_sub)

        # Dive deeper into this branch
        branch_results = greedy_branching(branched_grammar, rule_counter + 1)

        # Collect the final grammars
        all_final_grammars.extend(branch_results)

    return all_final_grammars


