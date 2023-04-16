import random
import argparse
from sorting import *

SORTING_ALGORITHMS = ['bubble', 'insertion', 'selection', 'cocktail']

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Sorting algorithm implementations')

    sorting_algo_group = parser.add_mutually_exclusive_group(required=True)
    for sorting_algo in SORTING_ALGORITHMS:

        abbrev = f'-{sorting_algo[0]}'
        full_option = f'--{sorting_algo}-sort'
        description = 'Use the {sorting_algo} sort algorithm'

        sorting_algo_group.add_argument(abbrev, full_option, 
                                        action='store_true', help=description)

    parser.add_argument('-n', type=int, 
                        help='number of ints to sort',
                        default=10)
    parser.add_argument('--max-value', type=int,
                        help='maximum value that can appear in the list to sort',
                        default=100)

    args = parser.parse_args()

    sort_options = [(arg, val) for arg, val in args._get_kwargs() if 'sort' in arg]
    nums = [random.randint(0, args.max_value) for i in range(args.n)]

    for algo, chosen in sort_options:
        if chosen:
            
            globals()[algo](nums)
            print(nums)
            exit(0)
