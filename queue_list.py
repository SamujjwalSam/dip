# coding=utf-8
"""
Implementing a Queue using a list type variable
__author__ = 'Samujjwal_Ghosh'
"""
import sys


def q_in(q_i):
    """
    inserts a value in the queue
    :param q_i:
    :return:
    """
    val = raw_input("Enter value: ")
    q_i.insert(0, val)


def q_out(q_o):
    """
    deletes a value from queue
    :param q_o:
    :return:
    """
    if q_o.__len__():
        #print "Removed: " + q_o[-1]
        ret = q_o[-1]
        del q_o[-1]
        return ret
    else:
        print "Queue empty."

if __name__ == '__main__':
    q = []
    user_input = raw_input("Enter choice; 0:exit, 1:insert, 2:delete: ")
    while user_input:
        assert isinstance(user_input, object)
        if user_input == '0':
            sys.exit(1)
        elif user_input == '1':
            q_in(q)
        elif user_input == '2':
            print "Removed: " + q_out(q)
        else:
            print q
        user_input = raw_input("Enter choice; 0:exit, 1:insert, 2:delete: ")