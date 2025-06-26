from itertools import product

def generate_lex_strings(alphabet, n):
    combinations = product(alphabet, repeat=n)

    strings = [''.join(p) for p in combinations]

    order_map = {char: i for i, char in enumerate(strings)}