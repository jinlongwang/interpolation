# -*- coding=utf-8 -*-
from MathUtils import MathUtils
from PolynomialFunction import *
from polynomiaSplineFuction import *


# noinspection PyMethodMayBeStatic
class SplineInterpolator(object):
    def interpolate(self, x, y):
        """

        :param x: []
        :param y: []
        :return:
        """
        if len(x) != len(y):
            raise ArgumentsException("lenth of x and y is diffrence")

        if len(x) < 3:
            raise ArgumentsException("lenth of x is less than 3")

        n = len(x) - 1
        MathUtils.checkOrder(x)

        h = []
        for i in range(n):
            h.append(x[i + 1] - x[i])

        mu = []
        z = []
        mu.append(float(0))
        z.append(float(0))
        # g = 0

        for i in range(1, n):
            # g = 2d * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1];
            g = float(2) * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
            mu.append(h[i] / g)
            # z[i] = (3d * (y[i + 1] * h[i - 1] - y[i] * (x[i + 1] - x[i - 1]) + y[i - 1] * h[i]) / (h[i - 1] * h[i]) - h[i - 1] * z[i - 1]) / g;
            z.append(float(3) * (y[i + 1] * h[i - 1] - y[i] * (x[i + 1] - x[i - 1]) + y[i - 1] * h[i]) / (h[i - 1] * h[i] - h[i - 1] * z[i - 1]) / g)

        b = [float(0)] * n  # linear: 线性
        c = [float(0)] * (n + 1)  # quadratic: 二次方程
        d = [float(0)] * n  # cubic: 多项式

        z.append(float(0))

        for j in range(n - 1, -1, -1):
            # c[j] = z[j] - mu[j] * c[j + 1];
            # b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2d * c[j]) / 3d;
            # d[j] = (c[j + 1] - c[j]) / (3d * h[j]);
            c[j] = z[j] - mu[j] * c[j + 1]
            b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + float(2) * c[j]) / float(3)
            d[j] = (c[j + 1] - c[j]) / (float(3) * h[j])

        polynomials = []
        coefficients = [0] * 4
        for i in range(n):
            coefficients[0] = y[i]
            coefficients[1] = b[i]
            coefficients[2] = c[i]
            coefficients[3] = d[i]
            polynomials.append(PolynomialFunction(coefficients))

        return PolynomiaSplineFuction(x, polynomials)
