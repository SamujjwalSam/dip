"""
Implementing a Stack using a list type variable
__author__ = 'Samujjwal_Ghosh'
"""
import sys


def push(stack):
    """
    Pushes the value into the list
    :param stack:
    :return:
    """
    user_value = raw_input("Enter value: ")
    stack.append(user_value)


def pop(stack):
    """
    Pops the last value
    :param stack:
    :return:
    """
    if stack.__len__():
        print "popped: " + stack[-1]
        del stack[-1]
    else:
        print "Stack empty."

if __name__ == "__main__":
    stack_list = []
    user_input = raw_input("Enter choice; 0:quit, 1:push, 2:pop: ")
    while user_input:
        assert isinstance(user_input, object)
        if user_input == '0':
            sys.exit(1)
        elif user_input == '1':
            push(stack_list)
        elif user_input == '2':
            pop(stack_list)
        else:
            print "\n".join(stack_list)
        user_input = raw_input("Enter choice; 0:quit, 1:push, 2:pop: ")