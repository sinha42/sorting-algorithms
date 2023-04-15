from typing import List

def swap(l, i, j):
    '''Swaps l[i] for l[j]'''
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def bubble_sort(l: List[int]):
    
    for i in range(len(l)):
        bubbleable = l[1:-i] if i > 0 else l[1:]
        for j in range(1, len(bubbleable)+1): #range returns half open range
            if(l[j-1] > l[j]):
                swap(l, j-1, j)

    return l

def insertion_sort(l: List[int]):
    
    print('insertion_sort')
    print(l)

def selection_sort(l: List[int]):
    
    print('selection_sort')
    print(l)

def cocktail_sort(l: List[int]):
    
    print('cocktail_sort')
    print(l)
