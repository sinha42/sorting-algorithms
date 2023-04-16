import inspect
from typing import List

def swap(l, i, j):
    '''Swap l[i] for l[j]'''

    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def bubble_sort(l: List[int]):
    
    print('bubble_sort')
    print(l)

def insertion_sort(l: List[int]):
    
    print('insertion_sort')
    print(l)

def selection_sort(l: List[int]):
    
    print('selection_sort')
    print(l)

def cocktail_sort(l: List[int]):
    
    for i in range(len(l)):
        
        '''
        explanation of ranges:
        forward range: on each even value of i, we advance 1 position farther at
        start of the range, bc by that point we have placed the next smallest 
        element at the front. We also shrink the end of the range because the
        last even value of i placed the greatest element at the end of the array
        backward range: Analogous to forward range, but we have to flip the
        direction in which we iterate.
        Note that range() creates a half open range
        '''
        ranges = (range(1+(i//2), len(l)-(i//2)), range(len(l)-2-(i//2), i//2, -1))
        cocktail_range = ranges[i&1]

        for j in cocktail_range:
            if(l[j-1] > l[j]):
                swap(l, j-1, j)

