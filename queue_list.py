# coding=utf-8
"""
Implementing a Queue using a list type variable
__author__ = 'Samujjwal_Ghosh'
"""
import sys


def q_in(q_i) :
    """
    inserts a value in the queue
    :param q_i:
    :return:
    """
    val = raw_input("Enter value: ")
    q_i.insert(0, val)


def q_out(q_o) :
    """
    deletes a value from queue
    :param q_o:
    :return ret:
    """
    if q_o.__len__() :
        ret = q_o[-1]
        del q_o[-1]
        return ret
    else :
        return None


if __name__ == '__main__' :
    q = []
    while 1 :
        user_input = raw_input("Enter choice; 1:insert, 2:delete, 3:print : ")
        assert isinstance(user_input, object)
        if user_input == '1' :
            q_in(q)
        elif user_input == '2' :
            del_val = q_out(q)
            if del_val is None :
                print "Queue empty."
            else :
                print "Removed: " + del_val
        elif user_input == '3' :
            print q
        else :
            sys.exit(1)