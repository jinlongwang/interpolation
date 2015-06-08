# -*- coding=utf-8 -*-
import copy
from myExcept import *
from bisect import bisect_left

# noinspection PyPep8Naming
class PolynomiaSplineFuction(object):

    __knots = []
    __polynomials = []
    __n = 0

    @property
    def knots(self):
        return self.__knots

    @property
    def Knots(self):
        return copy.copy(self.__knots)

    @property
    def polynomials(self):
        return self.__polynomials

    @property
    def n(self):
        return self.__n

    def __init__(self, _konts, polys):
        """
        public PolynomialSplineFunction(double[] _knots, PolynomialFunction[] polys)
        {
            if (_knots.Length < 2)
            {
                throw new ArgumentException("_knots.Length < 2");
            }
            if (_knots.Length - 1 != polys.Length)
            {
                throw new ArgumentException("_knots.Length - 1 != polys.Length");
            }
            if (!isStrictlyIncreasing(_knots))
            {
                throw new ArgumentException("_knots is not Strictly Increasing");
            }

            this.n = _knots.Length - 1;
            this.knots = new double[n + 1];
            Array.Copy(_knots, 0, this.knots, 0, n + 1);
            this.polynomials = new PolynomialFunction[n];
            Array.Copy(polys, 0, this.polynomials, 0, n);
        }
        :return:
        """
        if len(_konts) < 2:
            raise ArgumentsException("_knots.Length < 2")

        if len(_konts) - 1 != len(polys):
            raise ArgumentsException("_knots.Length - 1 != polys.Length")

        if not self.isStrictlyIncreasing(_konts):
            raise ArgumentsException("_knots is not Strictly Increasing")

        self.__n = len(_konts) - 1
        # self.__knots = _konts
        # self.__polynomials = polys
        self.__knots = copy.copy(_konts)
        self.__polynomials = copy.copy(polys)

    def value(self, v):
        """
        public double value(double v)
        {
            if (v < knots[0] || v > knots[n])
            {
                throw new ArgumentOutOfRangeException("v is out of range of knots[]");
            }
            int i = Array.BinarySearch(knots, v);
            if (i < 0)
            {
                i = -i - 2;
            }
            //This will handle the case where v is the last knot value
            //There are only n-1 polynomials, so if v is the last knot
            //then we will use the last polynomial to calculate the value.
            if (i >= polynomials.Length)
            {
                i--;
            }
            return polynomials[i].value(v - knots[i]);
        }
        :return:
        """
        if v < self.knots[0] or v > self.knots[self.n]:
            raise ArgumentsException("v is out of range of knots[]")

        i = binary_search(self.knots, v)
        if i < 0:
            i = -i - 1
        if i >= len(self.polynomials):
            i -= 1
        return self.polynomials[i].value(v - self.knots[i])

    def derivative(self):
        """
        public PolynomialSplineFunction derivative()
        {
            return polynomialSplineDerivative();
        }
        :return:
        """
        return self.polynomialSplineDerivative()

    def polynomialSplineDerivative(self):
        """
        public PolynomialSplineFunction polynomialSplineDerivative()
        {
            PolynomialFunction[] derivativePolynomials = new PolynomialFunction[n];
            for (int i = 0; i < n; i++)
            {
                derivativePolynomials[i] = polynomials[i].polynomialDerivative();
            }
            return new PolynomialSplineFunction(knots, derivativePolynomials);
        }
        :return:
        """
        derivativePolynomials = []
        for i in range(self.n):
            derivativePolynomials.append(self.polynomials[i].polynomialDerivative())
        return PolynomiaSplineFuction(self.knots, derivativePolynomials)

    @staticmethod
    def isStrictlyIncreasing(x):
        """
        private static bool isStrictlyIncreasing(double[] x)
        {
            for (int i = 1; i < x.Length; ++i)
            {
                if (x[i - 1] >= x[i])
                {
                    return false;
                }
            }
            return true;
        }

        :return:
        """
        pre = x[0]
        for i in x[1:]:
            if pre >= i:
                return False
            pre = i
        return True


def binary_search(a, x):
    pos = bisect_left(a, x)
    if pos < len(a) and a[pos] == x:
        return pos
    else:
        return -pos

if __name__ == '__main__':
    cc = PolynomiaSplineFuction.isStrictlyIncreasing([6, 5, 3])
    s = [1, 2, 3, 6, 7, 8, 11, 12]
    print len(s)
    print binary_search(s, -10), binary_search(s, 3), binary_search(s, 4), binary_search(s, 9), binary_search(s, 11), binary_search(s, 15)
    print cc
