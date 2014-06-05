"""
DiveIntoPython book codes ::

My programs

script options
--------------
--token :

author(s) : Samujjwal Ghosh
"""
import sys


def func(param):
    """take 3 arguments and prints them based on condition
    :param param:
    """  # doc_string
    print ("in func")
    (a, b, c) = param
    if a == 0:
        print b + c
    else:
        print a

if __name__ == "__main__":
    print sys.path
    params = (0, 1, 2)
    func(params)
    params = (5, 1, 2)
    print func.__doc__  # prints doc_string of the func
    
    dct = {"a": "0", "b": "1"}  # dictionary, methods: keys, values, items
    print "dict:" + dct["b"]
    dct["c"] = "2"
    print dct
    
    lst = ["l1", "l2", "l3"]  # list, methods: join, insert, append
    print [elm for elm in lst]  # list comprehension
    lst.insert(0, "l0")
    print [elm for elm in lst]
    print getattr(lst, 'pop')
    print [elm for elm in lst if elm == 'l2']  # list filtering

    tpl = ("t1", "t2", "t3")
    print tpl[-1]
    
    st = "this is a string"
    print st.split("s")
    #print type(st)
    #print dir(st)
    #print string.punctuation
    #print dir(string)
    #print dir(__builtin__)