import argparse
from sorting import *

SORTING_ALGORITHMS = ['bubble', 'insertion', 'selection', 'cocktail']

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Sorting algorithm implementations')

    sorting_algo_group = parser.add_mutually_exclusive_group(required=True)
    for sorting_algo in SORTING_ALGORITHMS:

        abbrev = f'-{sorting_algo[0]}'
        full_option = f'--{sorting_algo}-sort'
        sorting_algo_group.add_argument(abbrev, full_option, action='store_true')

    args = parser.parse_args()

    for algo, chosen in args._get_kwargs():
        if chosen:
            
            globals()[algo]()
            exit(0)

