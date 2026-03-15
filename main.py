from Greedy import greedy
from greedy_optimal import greedy_branching




def grammar_size(grammar):
    total_size = 0
    for token_list in grammar.values():
        total_size += len(token_list)
    return total_size

def print_grammar(grammar):
    print("\n--- Final Compressed Grammar ---")
    for rule_name, token_list in grammar.items():
        # Join the list of tokens into a single continuous string
        right_hand_side = "".join(token_list)

        # Print with the nice arrow formatting
        print(f"{rule_name} --> {right_hand_side}")
    print("--------------------------------\n")
    size = grammar_size(grammar)
    print('the size of this grammar is {}'.format(size))

def unary_string(n, character='a'):
    return character * n


import math


def run_asymptotic_ratio_experiment(max_n=100):
    """
    Runs the Greedy algorithm on unary strings from n=2 to max_n.
    Calculates the ratio: size / (3 * log_3(n))
    Prints the maximum ratio encountered.
    """
    max_ratio = 0
    n_at_max_ratio = 0

    print(f"Starting experiment for n=2 to {max_n}...")
    print("--------------------------------------------------")

    for n in range(2, max_n + 1):
        string = unary_string(n)
        final_grammar = greedy(string)
        size = grammar_size(final_grammar)
        ratio = size / (3 * math.log(n, 3))
        if ratio > max_ratio:
            max_ratio = ratio
            n_at_max_ratio = n
            print(f"New Max Ratio: {max_ratio:.6f} | Found at n = {n:<5} | Grammar Size = {size}")

        if n % 1000 == 0:
            print(f"... still processing, currently at n = {n} ...")

    print("--------------------------------------------------")
    print("EXPERIMENT COMPLETE")
    print(f"Absolute Maximum Ratio: {max_ratio:.6f}")
    print(f"Occurred at string length (n): {n_at_max_ratio}")
    print("--------------------------------------------------")

    return max_ratio, n_at_max_ratio


def run_optimal_greedy(input_sequence):
    """
    Initializes the branching search and returns the absolute smallest grammar
    found across all possible tie-breaking paths.
    """
    if isinstance(input_sequence, str):
        initial_grammar = {'A0': list(input_sequence)}
    else:
        initial_grammar = {'A0': list(input_sequence)}

    all_possible_grammars = greedy_branching(initial_grammar, rule_counter=1)

    # Find the grammar with the minimum size
    best_grammar = min(all_possible_grammars, key=grammar_size)

    print(f"Explored {len(all_possible_grammars)} different tie-breaking paths.")
    return best_grammar


def run_optimal_asymptotic_experiment(max_n=30):
    """
    Runs the Optimal (Branching) Greedy algorithm on unary strings.
    Calculates the ratio: size / (3 * log_3(n))
    """
    max_ratio = 0
    n_at_max_ratio = 0

    print(f"Starting OPTIMAL experiment for n=2 to {max_n}...")
    print("WARNING: Branching search is exponential. This will get slow as n grows!")
    print("--------------------------------------------------")

    for n in range(800, max_n + 1):
        string = unary_string(n)

        final_grammar = run_optimal_greedy(string)

        size = grammar_size(final_grammar)

        ratio = size / (3 * math.log(n, 3))

        if ratio > max_ratio:
            max_ratio = ratio
            n_at_max_ratio = n
            print(f"New Max Ratio: {max_ratio:.6f} | Found at n = {n:<5} | Grammar Size = {size}")

    print("--------------------------------------------------")
    print("OPTIMAL EXPERIMENT COMPLETE")
    print(f"Absolute Maximum Ratio: {max_ratio:.6f}")
    print(f"Occurred at string length (n): {n_at_max_ratio}")
    print("--------------------------------------------------")

    return max_ratio, n_at_max_ratio



#run_optimal_asymptotic_experiment(1000)
letsgo = unary_string(2187)
print_grammar(greedy(letsgo))


