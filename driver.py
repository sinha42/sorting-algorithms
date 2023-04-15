
from sorting import *

if __name__ == '__main__':
    
    sorts = ['bubble', 'insertion', 'selection', 'cocktail']
    for sort_name in sorts:
        globals()[sort_name+'_sort']()
