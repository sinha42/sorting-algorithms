from typing import List

def swap(l, i, j):
    '''Swaps l[i] for l[j]'''

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
    
    for i in range(len(l)):

        max_index = i # bug 
        #max_index = 0

        for j in range(1, len(l) - i):
            if(l[max_index] < l[j]):
                max_index = j
            
        swap(l, max_index, (len(l) - 1 - i))

def cocktail_sort(l: List[int]):
    
    print('cocktail_sort')
    print(l)
