from typing import List

def swap(l, i, j):
    '''Swaps l[i] with l[j]'''
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def bubble_sort(l: List[int]):
    
    print('bubble_sort')
    print(l)

def insertion_sort(l: List[int]):
    
    for i in range(len(l)):
        for j in range(len(l[:i]), 0, -1):
            if(l[j] < l[j-1]):
                swap(l, j, j-1)

def selection_sort(l: List[int]):
    
    print('selection_sort')
    print(l)

def cocktail_sort(l: List[int]):
    
    print('cocktail_sort')
    print(l)
