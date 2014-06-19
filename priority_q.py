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

        try:
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
    priority_q = {}
    while 1 :
        try :
            user_input = int(raw_input("Enter choice; 1:insert, 2:delete,"
                                       " 3:print : "))
        except ValueError :
            try:
                retry = raw_input("Empty value entered; retry? (y/n; "
                                  "default:n): ")
                if retry == 'y':
                    continue
                sys.exit(1)
            except ValueError:
                sys.exit(1)

        if user_input == 1 :
            priority_in(priority_q)
        elif user_input == 2 :
            priority_out(priority_q)
        elif user_input == 3 :
            print priority_q
        else :
            try :
                user_input = int(raw_input("Invalid Input; retry? (y/n; "
                                           "default:n): "))
            except ValueError :
                try:
                    retry = raw_input("Empty value entered; retry? (y/n; "
                                      "default:n): ")
                    if retry == 'y':
                        continue
                    sys.exit(1)
                except ValueError:
                    sys.exit(1)