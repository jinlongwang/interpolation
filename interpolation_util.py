# -*- coding=utf-8 -*-

from SplineInterpolator import SplineInterpolator

__author__ = 'balin'


# noinspection PyPep8Naming
def generateSplineFunction(array1, array2):

    interpolator = SplineInterpolator()
    return interpolator.interpolate(array1, array2)


def interpolate(spline, x):
    # noinspection PyBroadException
    try:
        return spline.value(x)
    except:
        knots = spline.Knots
        return spline.value(knots[0 if x < knots[0] else spline.n - 1])
