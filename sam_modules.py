# coding=utf-8
"""
INFO:
DESC:
script options
--------------
--param : parameter list

Created by Samujjwal_Ghosh on 19-Jun-14.

__author__ : Samujjwal Ghosh
__version__ = ": 1 $"
__date__ = "$"
__copyright__ = "Copyright (c) 2014 Samujjwal Ghosh"
__license__ = "Python"
"""

import os

call_pass = 'CALLPASS'
call_fail = 'CALLFAIL'


class ReturnValue(object) :
    """
    Contains return values of the call
    """

    def __init__(self, call_status, val=None, msg="") :
        self.call_status = call_status
        self.msg = msg
        self.val = val


def type_check(param_list, param_type_list) :
    """
    checks the parameter types
    :param param_list:
    :param param_type_list:
    :return:
    """
    for param_name, param_type in param_list, param_type_list :
        if type(param_name) != param_type :
            msg = "Type [%s] mismatch for param [%s]" % param_type, param_name
            return ReturnValue(call_fail, msg)
    return ReturnValue(call_pass)


def int_input(to_print) :
    """
    Takes integer input from console
    :param to_print:
    :return val:
    """
    while 1 :
        try :
            val = int(raw_input(to_print))
            print val
        except ValueError :
            retry = raw_input("Empty or non-integer value entered; retry? ("
                              "y/n; default:n): ")
            if retry == 'y' :
                continue
            else :
                msg = "Entered [%s]; Returning..." % retry
                return ReturnValue(call_fail, retry, msg=msg)
        return ReturnValue(call_pass, val=val)


def str_input(to_print) :
    """
    Takes string input from console
    :param to_print:
    :return val:
    """
    while 1 :
        val = raw_input(to_print)
        if val == "" :
            retry = raw_input("Empty value entered; retry? (y/n; default:n): ")
            if retry == 'y' :
                continue
            else :
                msg = "Entered [%s]; Returning..." % retry
                return ReturnValue(call_fail, retry, msg=msg)
        return ReturnValue(call_pass, val=val)


def file_check(file_name, mode='r') :
    """
    takes file name check its existence and returns file handle
    :param file_name:
    :param mode:
    :return fh:
    """
    method = 'access'

    if mode[0] == 'w' :
        method = 'write'

    if os.path.isfile(file_name) and getattr(os, method)(file_name, os.R_OK) :
        print "File exists and is %sable; Opening file..." % method
        try :
            fh = open(file_name, mode)
        except IOError :
            msg = "Could not open file [%s]; \n Returning... " % file_name
            return ReturnValue(call_fail, msg=msg)
        return ReturnValue(call_pass, fh)
    else :
        msg = "Either file is missing or is not %sable; Returning..." % method
        return ReturnValue(call_fail, msg=msg)


if __name__ == "__main__" :
    print int_input("Enter a number: ")
    print str_input("Enter a string: ")
    fh = file_check('READMe.MD').val
    print fh.read()