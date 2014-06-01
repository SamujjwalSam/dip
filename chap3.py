import sys

def func (params) :
    """take 3 arguments and prints them based on condition""" #doc_string
    print ("in func")
    (a,b,c) = params
    if a == 0 :
        print b + c
    else :
        print a

if __name__ == "__main__" :
    print sys.path
    params = (0,1,2)
    func (params)
    params = (5,1,2)
    print func.__doc__ #prints doc_string of the func
    
    dict = {"a":"0","b":"1"} # dictionary, methonds: keys, values, items
    print "dict:" + dict["b"]
    dict["c"] = "2"
    print dict
    
    list = ["l1","l2","l3"] # list, methods: join, insert, append
    print [elm for elm in list] # list comprehention
    list.insert(0,"l0")
    print [elm for elm in list]
    
    tuple = ("t1","t2","t3")
    print tuple[-1]
    
    str = "this is a string"
    print str.split("s")