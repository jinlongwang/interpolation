# -*- coding=utf-8 -*-
"""
自定义异常
"""


class MyError(Exception):
    pass


class ArgumentsException(MyError):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "argument error %s" % self.msg
