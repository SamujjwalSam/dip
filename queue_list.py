# coding=utf-8
"""
Implementing a Queue using a list type variable
__author__ = 'Samujjwal_Ghosh'
"""
import sys
import sam_modules

call_pass = tuple(['PASS'])
call_fail = tuple(['FAIL'])
call_err = tuple(['ERROR'])


class Q(object):
    """
    Class used as queue
    """

    def __init__(self):
        self.q = []

    def q_in(self, v=None):
        """
        inserts a value in the queue
        :param v:
        :return:
        """
        if v:
            self.q.insert(0, v)
        else:
            val = sam_modules.str_input("Enter value: ")
            if val.call_status == call_pass:
                self.q.insert(0, val.val)

    def q_out(self):
        """
        deletes a value from queue
        :return ret:
        """
        if self.q.__len__():
            ret = self.q[-1]
            try:
                del self.q[-1]
            except:
                pass
            return ret
        else:
            return None

    def q_print(self):
        """
        prints the q
        """
        print self.q


if __name__ == '__main__':
    queue = Q()
    while 1:
        user_input = sam_modules.str_input("Enter choice; 1:insert, 2:delete, "
                                           "3:print : ")
        if user_input.val == '1':
            queue.q_in()
        elif user_input.val == '2':
            del_val = queue.q_out()
            if del_val is None:
                print "Queue empty."
            else:
                print "Removed: [%s]" % del_val
        elif user_input.val == '3':
            print queue.q_print()
        else:
            sys.exit(1)