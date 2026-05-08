from collections import defaultdict

# The global cache
ultra_worst_cache = {}


def greedy_worst_ultra(rules):
    """
    Returns the WORST-CASE grammar (tuple of strings).
    Uses exact mathematical state matching to prevent cache collisions.
    """
    # 1. Exact tuple matching (100% accurate, no collisions)
    if rules in ultra_worst_cache:
        return ultra_worst_cache[rules]

    max_len = max((len(r) for r in rules), default=0)
    best_candidates = []
    max_savings = -1

    # 2. Fast substring sieve
    for L in range(2, max_len + 1):
        counts = defaultdict(int)
        for r in rules:
            for i in range(len(r) - L + 1):
                counts[r[i:i + L]] += 1

        candidates = [sub for sub, c in counts.items() if c >= 2]

        if not candidates:
            break

        for sub in candidates:
            k = sum(r.count(sub) for r in rules)
            if k < 2:
                continue

            current_savings = (L - 1) * k - L

            if current_savings > max_savings:
                max_savings = current_savings
                best_candidates = [sub]
            elif current_savings == max_savings and current_savings > -1:
                best_candidates.append(sub)

    # 3. Base Case: Return the grammar itself
    if max_savings <= -1 or not best_candidates:
        ultra_worst_cache[rules] = rules
        return rules

    worst_grammar = rules
    worst_len = sum(len(r) - 1 for r in rules)

    # Start at a high Unicode point to avoid overlapping with 'a' or 'b'
    new_char = chr(0x1000 + len(rules))

    # 4. Branch out into parallel universes
    for sub in best_candidates:
        # C-Engine string replace
        new_rules = tuple(r.replace(sub, new_char) for r in rules)
        new_rules = new_rules + (sub,)

        branch_grammar = greedy_worst_ultra(new_rules)
        branch_len = sum(len(r) - 1 for r in branch_grammar)

        # Track the absolute worst (longest) grammar
        if branch_len > worst_len:
            worst_len = branch_len
            worst_grammar = branch_grammar

    # 5. Cache the worst grammar found from this state
    ultra_worst_cache[rules] = worst_grammar
    return worst_grammar


def print_ultra_grammar(final_rules):
    """
    Translates the Unicode strings back into a readable grammar and prints it.
    """
    print("\n--- Final Worst-Case Grammar ---")
    for i, rule in enumerate(final_rules):
        readable_rule = ""
        for char in rule:
            char_code = ord(char)
            # If it's a generated rule character
            if char_code >= 0x1000:
                rule_num = char_code - 0x1000 + 1
                readable_rule += f"A{rule_num} "
            # If it's a base character ('a' or 'b')
            else:
                readable_rule += f"{char} "

        rule_name = "A0" if i == 0 else f"A{i}"
        print(f"{rule_name} -> {readable_rule.strip()}")

    length = sum(len(r) - 1 for r in final_rules)
    print("--------------------------------")
    print(f"Total Chain Length: {length}\n")
def fibonacci_word(i):
    if i < 1:
        raise ValueError("Index i must be 1 or greater.")
    if i == 1:
        return "b"
    if i == 2:
        return "a"

    f_minus_2 = "b"  # F_1
    f_minus_1 = "a"  # F_2
    current_f = ""

    for _ in range(3, i + 1):
        current_f = f_minus_1 + f_minus_2
        f_minus_2 = f_minus_1
        f_minus_1 = current_f

    return current_f


def run_ultra_worst_experiment(fib_index):
    global ultra_worst_cache
    ultra_worst_cache.clear()

    fib_string = fibonacci_word(fib_index)
    initial_rules = (fib_string,)

    # Run the corrected algorithm
    worst_grammar = greedy_worst_ultra(initial_rules)

    # Print it so you can verify the results
    print_ultra_grammar(worst_grammar)

    return sum(len(r) - 1 for r in worst_grammar)

# Test it:
run_ultra_worst_experiment(15)