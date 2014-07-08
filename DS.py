# coding=utf-8
# !/usr/bin/python
"""
__synopsis__    : 
__description__ : 
__project__     : dip
__author__      : Samujjwal_Ghosh
__version__     : ":  "
__date__        : "30-Jun-14"
__copyright__   : "Copyright (c) 2014 Samujjwal_Ghosh"
__license__     : "Python"

__classes__     :
    
__variables__   :
    
__methods__     :
"""

import sys
import sam_modules

# todo : 


class Class(object):
    """
    hello
    """

    def __init__(self):
        pass


def merge_sort(alist):
    """
    Merge sort in python
    :param alist:
    """
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    print("Merging ", alist)


if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(alist)
    print(alist)