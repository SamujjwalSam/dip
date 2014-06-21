# coding=utf-8
# !/usr/bin/python
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
import types
import inspect

call_pass = 'PASS'
call_fail = 'FAIL'
call_err = 'ERROR'

str_type = types.StringType


class ReturnValue(object) :
    """
    Contains return values of the call
    """

    call_stack = []

    def __init__(self, call_status, val=None, msg="", method_msg=None) :
        self.call_status = call_status
        self.msg = msg
        self.val = val
        self.val_type = type(val)
        self.method_msg = method_msg


def is_empty(param_list) :
    """

    :param param_list:
    :return:
    """
    method_name = '##' + os.path.basename(__file__) + ':is_empty'
    print method_name
    ReturnValue.call_stack.append(method_name)

    msg = "[%s]: non-empty" % inspect.currentframe().f_back.f_lineno

    if not param_list.__len__() :
        msg = "[%s]: Empty value provided for param_list"
        return ReturnValue(call_status=call_err, msg=msg)
    elif param_list.__len__() == 1 :
        if param_list :
            msg = "[%s]: [%s] non-empty." % (inspect.currentframe(
            ).f_back.f_lineno, param_list)
            return ReturnValue(call_status=call_pass, msg=msg)
        else :
            msg = "[%s]: [%s] Empty" % (inspect.currentframe().f_back.f_lineno,
                                        param_list)
            return ReturnValue(call_status=call_fail, msg=msg)
    else :
        for param in param_list :
            if not param :
                msg = "[%s]: Empty value provided for parameter [%s]" % \
                      inspect.currentframe().f_back.f_lineno, param
                return ReturnValue(call_status=call_fail, msg=msg)
    return ReturnValue(call_status=call_fail, msg=msg)


def type_check(param_values, param_types) :
    """
    checks the parameter types
    :param param_values:
        Type: list
        Required
        Read Only
    :param param_types:
        Type: list
        Required
        Read Only
    :return Object: return object of type [ReturnValue]
        Type: object
    """
    method_name = '##' + os.path.basename(__file__) + ':type_check'
    print method_name
    ReturnValue.call_stack.append(method_name)

    i = 0

    if (not isinstance(param_values, types.ListType)) or (not isinstance(
            param_types, types.ListType)) :
        msg = "[%s]: Provided parameters are not <list> type " % \
              inspect.currentframe().f_back.f_lineno
        return ReturnValue(call_status=call_err, msg=msg)

    if (not param_values) or (not param_types) :
        msg = "[%s]: Empty list provided for Required parameter" % \
              inspect.currentframe().f_back.f_lineno
        return ReturnValue(call_status=call_err, msg=msg)

    for param_val, param_type in zip(param_values, param_types) :
        i += 1
        if type(param_val) != getattr(types, param_type) :  # checking type
            # of param_val with builtin types of module types for all elements
            msg = "[%s]: Type mismatch for param no: [%d]; Expected: [%s]" \
                  " Provided: [%s]" % (inspect.currentframe(
            ).f_back.f_lineno, i, param_type, type(param_val))
            return ReturnValue(call_status=call_fail, val=i, msg=msg)
    return ReturnValue(call_status=call_pass, msg='Type check successful for '
                                                  'all parameters.')


def int_input(to_print) :
    """
    Takes integer input from console
    :param to_print: Prints
        Type: str
        Required
        Read Only
    :return Object: return object of type [ReturnValue]
        Type: object
    """
    method_name = '##' + os.path.basename(__file__) + ':int_input:'
    print method_name
    ReturnValue.call_stack.append(method_name)

    if not to_print :
        msg = "Empty string passed."
        return ReturnValue(call_status=call_err, msg=msg)

    tc = type_check([to_print], ['StringType'])
    if (tc.call_status == call_fail) or (tc.call_status == call_err) :
        return ReturnValue(call_status=tc.call_status, msg=tc.msg)

    while 1 :
        try :
            val = int(raw_input(to_print))
            msg = "[%s]: Retrieved value [%s] successfully" % \
                  (inspect.currentframe().f_back.f_lineno, val)
            return ReturnValue(call_status=call_pass, val=val, msg=msg)
        except ValueError :
            retry = raw_input("Empty or non-integer value entered; retry? ("
                              "y/n; default:n): ")
            if retry == 'y' :
                continue
            else :
                msg = "[%s]: Entered [%s]; Returning..." % \
                      (inspect.currentframe().f_back.f_lineno, retry)
                return ReturnValue(call_status=call_fail, msg=msg)


def str_input(to_print) :
    """
    Takes string input from console
    :param to_print: Prints
        Type: str
        Required
        Read Only
    :return Object: return object of type [ReturnValue]
        Type: object
    """
    method_name = '##' + os.path.basename(__file__) + ':str_input'
    print method_name
    ReturnValue.call_stack.append(method_name)

    if not to_print :
        msg = "Empty string passed."
        return ReturnValue(call_status=call_err, msg=msg)

    tc = type_check([to_print], ['StringType'])
    if (tc.call_status == call_fail) or (tc.call_status == call_err) :
        return ReturnValue(call_status=tc.call_status, msg=tc.msg)

    while 1 :
        val = raw_input(to_print)
        if val == "" :
            retry = raw_input("Empty value entered; retry? (y/n; default:n): ")
            if retry == 'y' :
                continue
            else :
                msg = "[%s]: Entered [%s]; Returning..." % \
                      (inspect.currentframe().f_back.f_lineno, retry)
                return ReturnValue(call_fail, msg=msg)
        return ReturnValue(call_pass, val=val)


def file_check(file_name, mode='r', content=None, print_file=0) :
    """
    takes file name check its existence and returns file handle
    :param print_file:if 1, then prints the content of file if mode != 'w'
    not 'a'
        Type: int
        Optional
        Read Only
    :param content:if not None, then append [content] to the file if mode != 'r'
        Type: str
        Optional
        Read Only
    :param file_name: Name of the file to open;
        Type: str
        Required
        Read Only
    :param mode: File open mode
        Type: str
        Required
        Read Only
    :return Object: return object of type [ReturnValue]
        Type: object
    """
    method_name = '##' + os.path.basename(__file__) + ':file_check'
    print method_name
    ReturnValue.call_stack.append(method_name)

    if file_name :
        msg = '[%s]: Empty value provided for Required parameter' % \
              inspect.currentframe().f_back.f_lineno
        return ReturnValue(call_status=call_fail, msg=msg)
    if mode :
        msg = '[%s]: Empty value provided for Required parameter' % \
              inspect.currentframe().f_back.f_lineno
        return ReturnValue(call_status=call_fail, msg=msg)

    val = None
    status = call_fail

    if os.path.isfile(file_name) :
        print "File [%s] exists." % file_name
        if mode.find('w') or mode.find('a') :
            if os.write(file_name, os.W_OK) :
                msg = "File [%s] available for writing." % file_name
                status = call_pass
            else :
                msg = "File [%s] not available for writing." % file_name
        else :
            if os.access(file_name, os.R_OK) :
                msg = "File [%s] available for reading." % file_name
                status = call_pass
            else :
                msg = "File [%s] not available for reading." % file_name
    else :
        msg = "Could not locate file [%s]." % file_name

    if status == call_pass :  # will only execute if file exists and accessible
        try :
            val = open(file_name, mode)
            if print_file == 1 and (mode != ('w' or 'a')) :  # can not read file
                # if mode is exactly 'w' or 'a'.
                print '[' + val.read() + ']'
            if content and (mode.find('w') or mode.find('a')) :  # will write
                # only if content is defined and mode is either 'w' or 'a' or
                # 'w+' or 'a+'.
                print "writing content \"[%s]\" to file [%s]" % (content,
                                                                 file_name)
                val.write(content)
        except IOError :
            msg = "Could not open file [%s]; \n Returning... " % file_name

        status = call_pass
    else :
        msg = "Either file [%s] is missing or is not accessible;" % file_name

    return ReturnValue(status, val=val, msg=msg)


if __name__ == "__main__" :  # for unit testing purposes only; will not execute
    # if module API call.
    user_input = int_input("Enter a number: ")
    user_input = str_input('hello: ')
    # print user_input.call_stack
    print user_input.call_status
    print user_input.msg
    print user_input.val

    # print str_input("Enter a string: ")
    #f = file_check('READMe.txt', 'w', 'trying', 1).val
    #print fh.read()