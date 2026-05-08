from non_overlapping_counter import count_non_overlapping
from replace_token import replace_tokens
from find_substring import find_substrings
import copy


def greedy_worst_branching(grammar, rule_counter=1):
    candidates = find_substrings(grammar)

    if not candidates:
        return [grammar]

    best_candidates = []
    # 1. Change initialization to 0
    max_savings = 0

    for sub in candidates:
        L = len(sub)
        k = count_non_overlapping(grammar, sub)

        if k < 2:
            continue

        current_savings = (L - 1) * k - L

        if current_savings > max_savings:
            max_savings = current_savings
            best_candidates = [sub]

        # 2. Change the tie-breaker floor to > 0
        elif current_savings == max_savings and current_savings > 0:
            best_candidates.append(sub)  # Log the tie

    # 3. Exit if max_savings is 0 or less
    if max_savings <= 0 or not best_candidates:
        return [grammar]

    all_final_grammars = []
    new_rule_name = f'A{rule_counter}'

    for best_sub in best_candidates:
        branched_grammar = copy.deepcopy(grammar)
        replace_tokens(branched_grammar, best_sub, new_rule_name)
        branched_grammar[new_rule_name] = list(best_sub)

        branch_results = greedy_worst_branching(branched_grammar, rule_counter + 1)
        all_final_grammars.extend(branch_results)

    return all_final_grammars