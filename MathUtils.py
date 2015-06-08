# -*- coding=utf-8 -*-
from myExcept import *

"""
工具类
"""


# noinspection PyPep8Naming
class MathUtils(object):

    def __init__(self):
        pass

    @staticmethod
    def checkOrder(val, direction=0, strict=True):
        """

        :param val: []
        :param direction: int 0降序，1升序
        :param strict: bool
        :return:
        """
        previous = val[0]
        ok = True
        for i in val[1:]:
            if direction == 0:
                if strict:
                    if i <= previous:
                        ok = False
                else:
                    if i < previous:
                        ok = False

            elif direction == 1:
                if strict:
                    if i >= previous:
                        ok = False
                else:
                    if i > previous:
                        ok = False
            else:
                raise ArgumentsException("args error")
            if not ok:
                raise ArgumentsException("array is not Strictly ordered")
            previous = i

if __name__ == '__main__':
    MathUtils.checkOrder([1, 2, 3], 0)
