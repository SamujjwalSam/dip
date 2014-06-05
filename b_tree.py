# coding=utf-8
"""
Implementing a Binary tree using a list type variable
__author__ = 'Samujjwal_Ghosh'
"""
import sys

import queue_list


#todo: implement Binary tree


def put(q, user_input):
    """

    :param q:
    :param user_input:
    :return:
    """
    if user_input == 1:
        getattr(queue_list, 'q_in')(q)
    elif user_input == 2:
        print "Removed: " + getattr(queue_list, 'q_out')(q)  # using getattr
        # calling the method in module queue_list; alt: queue_list.q_out(q)
    else:
        print q
    return 1


def exiting(q, user_input):
    """

    :param q:
    :param user_input:
    :return:
    """
    user_input and put(q, user_input) or sys.exit(1)

if __name__ == "__main__":
    print "binary tree"
    q = []
    while 1:
        user_input = input("Enter choice; 0:exit, 1:insert, 2:delete: ")
        exiting(q, user_input)