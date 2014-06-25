# coding=utf-8
"""
__synopsis__    : Implementing a priority queue
__description__ :
__project__     : dip
__author__      : Samujjwal_Ghosh
__version__     : " 1.0 "
__date__        : "25-Jun-14"
__copyright__   : "Copyright (c) 2014 Samujjwal_Ghosh"
__license__     : "Python"

__classes__     :

__variables__   :

__methods__     :
    priority_in
    priority_out
"""

import sys

import sam_modules


def priority_in(priority_q):
    """
    inserts a priority and value in the queue
    :param priority_q:
    :return:
    """
    priority = sam_modules.int_input("Enter priority: ").val

    if priority in priority_q.keys(): # todo change here
        overwrite = sam_modules.str_input("Priority already exists; Overwrite? "
                                          "Y/N; Default:Y : ").val
        if overwrite.lower() == 'n':
            return

    value = sam_modules.int_input("Enter value: ").val
    if value.call_status == 'PASS':
        priority_q[priority] = value


def priority_out(priority_q):
    """
    deletes the lowest priority value from queue
    :param priority_q:
    :return:
    """
    if priority_q.__len__():
        del_prio = max(priority_q.keys())
        del_val = priority_q[del_prio]
        del priority_q[del_prio]
        print "Deleted Lowest priority [%d] value from Queue: [%s]" % (del_prio,
                                                                       del_val)
    else:
        print "Queue empty."
        return None


if __name__ == "__main__":
    priority_q = []
    user_input = sam_modules.int_input("Enter choice; 1:insert, 2:delete,"
                                       " 3:print : ").val
    if user_input == 1:
        priority_in(priority_q)
    elif user_input == 2:
        priority_out(priority_q)
    elif user_input == 3:
        print priority_q
    else:
        print "Invalid input; Exiting..."
        sys.exit(1)