# coding=utf-8
"""
INFO: Implementing a priority queue

DESC: a Priority queue using lists with duplicate priorities

script options
--------------
--param : parameter list

Created by Samujjwal_Ghosh on 18-Jun-14.

__author__ : Samujjwal Ghosh
__version__ = ": 1 $"
__date__ = "$"
__copyright__ = "Copyright (c) 2014 Samujjwal Ghosh"
__license__ = "Python"
"""

import sys
import types


def priority_in(priority_q) :
    """
    inserts a priority and value in the queue
    :param priority_q:
    :return:
    """
    try :
        priority = int(raw_input("Enter priority: "))
    except ValueError :
        print "Empty Priority; Exiting..."
        sys.exit(1)

    if types.IntType == type(priority) :
        if priority in priority_q.keys() :
            overwrite = raw_input("Priority already exists; Overwrite? Y/N; "
                                  "Default:Y : ")
            if overwrite.lower() == 'n' :
                return

        try :
            value = int(raw_input("Enter value: "))
            priority_q[priority] = value
        except ValueError :
            print "Empty Value; Exiting..."
            sys.exit(1)
    else :
        print "priority must be integer."


def priority_out(priority_q) :
    """
    deletes the lowest priority value from queue
    :param priority_q:
    :return:
    """
    if priority_q.__len__() :
        del_prio = max(priority_q.keys())
        del_val = priority_q[del_prio]
        del priority_q[del_prio]
        print "Deleted Lowest priority [%d] value from Queue: [%s]" % (del_prio,
                                                                       del_val)
    else :
        print "Queue empty."
        return None


if __name__ == "__main__" :
    priority_q = []
    while 1 :
        try :
            user_input = int(raw_input("Enter choice; 1:insert, 2:delete,"
                                       " 3:print : "))
        except ValueError :
            print "Empty input; Exiting..."
            sys.exit(1)

        if user_input == 1 :
            priority_in(priority_q)
        elif user_input == 2 :
            priority_out(priority_q)
        elif user_input == 3 :
            print priority_q
        else :
            print "Invalid input; Exiting..."
            sys.exit(1)