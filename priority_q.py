# coding=utf-8
"""
Implementing a priority queue using a dictionary variable
__note__  = 'duplicate priority can not exist'
__author__ = 'Samujjwal_Ghosh'
"""
import sys
import types


def priority_in(priority_q) :
    """
    inserts a priority and value in the queue
    :param priority_q:
    :return:
    """
    priority = input("Enter priority: ")
    if types.IntType == type(priority) :
        if priority in priority_q.keys() :
            overwrite = input("Priority already exists; Overwrite? No:0 "
                              "Yes:others; Default: No")
            if not overwrite :
                return
        value = input("Enter value: ")
        priority_q[priority] = value


    else :
        print "priority must be integer."


def priority_out(priority_q) :
    """
    deletes the lowest priority value from queue
    :param priority_q:
    :return:
    """
    if priority_q.__len__() :
        del priority_q[max(priority_q.keys())]
    else :
        return None


if __name__ == "__main__" :
    priority_q = {}
    while 1 :
        user_input = input("Enter choice; 1:insert, 2:delete, 3:print : ")
        if user_input == 1 :
            priority_in(priority_q)
        elif user_input == 2 :
            priority_out(priority_q)
        elif user_input == 3 :
            print priority_q
        else :
            sys.exit(1)
