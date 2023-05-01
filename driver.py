import random
import sorting
import argparse
import tkinter as tk

SORTING_ALGORITHMS = ['bubble', 'insertion', 'selection', 'cocktail']

class SortingApplication(tk.Frame):
    
    def __init__(self, n, max_value, master=None):

        super().__init__(master)

        self.n = n
        self.max_value = max_value
        self.master = master

        self.original_list_label = tk.Label(self, text='[]')
        self.original_list_label.pack(side='top')

        self.sorted_list_label = tk.Label(self, text='')
        self.sorted_list_label.pack(side='top')

        self.create_buttons()
        self.pack()

    def create_buttons(self):
        
        sorting_algorithm_fns = vars(sorting)

        def create_button_action(full_sorting_algo_name):
            def button_action():
                nums = [random.randint(0, self.max_value) for _ in range(self.n)]
                self.original_list_label['text'] = nums
                sorting_algorithm_fns[full_sorting_algo_name](nums)
                self.sorted_list_label['text'] = nums

            return button_action

        for algo_name in SORTING_ALGORITHMS:
            
            sorting_button = tk.Button(self)
            full_sorting_algo_name = f'{algo_name}_sort'

            sorting_button['text'] = full_sorting_algo_name
            sorting_button['command'] = create_button_action(full_sorting_algo_name)

            sorting_button.pack(side='left')
            self.__dict__[f'{algo_name}_button'] = sorting_button

if __name__ == '__main__':
    
    print('Thanks for using this :)')
    
    parser = argparse.ArgumentParser(description='Sorting algorithm implementations')

    sorting_algo_group = parser.add_mutually_exclusive_group(required=True)
    for sorting_algo in SORTING_ALGORITHMS:

        abbrev = f'-{sorting_algo[0]}'
        full_option = f'--{sorting_algo}-sort'
        description = 'Use the {sorting_algo} sort algorithm'

        sorting_algo_group.add_argument(abbrev, full_option, 
                                        action='store_true', help=description)
    sorting_algo_group.add_argument('-g', '--gui', action='store_true',
                                    help='Launch GUI instead of using command line')

    parser.add_argument('-n', type=int, help='number of ints to sort', default=10)
    parser.add_argument('--max-value', type=int,
                        help='maximum value that can appear in the list to sort',
                        default=100)
    args = parser.parse_args()

    # create GUI application
    if args.gui:

        root = tk.Tk()
        app = SortingApplication(args.n, args.max_value, master=root)
        app.master.title('Sorting')
        app.mainloop()

    # command line version
    else:
        
        nums = [random.randint(0, args.max_value) for i in range(args.n)]
        print(nums)

        sort_options = [(arg, val) for arg, val in args._get_kwargs() if 'sort' in arg]

        for algo, chosen in sort_options:
            if chosen:
                
                vars(sorting)[algo](nums)
                exit(0)
