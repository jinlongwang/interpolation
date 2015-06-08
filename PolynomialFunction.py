# -*- coding=utf-8 -*-
import copy
from myExcept import *


# noinspection PyPep8Naming
class PolynomialFunction(object):
    __coefficients = []

    def __init__(self, c):
        """

        :param c: []
        :return:
        """
        n = len(c)
        if n == 0:
            raise ArgumentsException("数组为空")

        while n > 1 and c[n - 1] == 0:
            n -= 1

        self.__coefficients = copy.copy(c[:n])

    @property
    def coefficients(self):
        return self.__coefficients

    def value(self, x):
        """

        :return:
        """
        return self.evaluate(self.coefficients, x)

    def degree(self):
        return len(self.coefficients) - 1

    @staticmethod
    def evaluate(coefficients, argument):
        """
        double result = coefficients[n - 1];
            for (int j = n - 2; j >= 0; j--)
            {
                result = argument * result + coefficients[j];
            }
            return result;
        :param coefficients:
        :param argument:
        :return:
        """

        if len(coefficients) == 0:
            raise ArgumentsException("数组为空")
        result = coefficients[-1]
        for i in coefficients[-2::-1]:
            result = argument * result + i
        return result

    def add(self, p):
        """
        public virtual PolynomialFunction add(PolynomialFunction p)
        {

            // identify the lowest degree polynomial
            //JAVA TO C# CONVERTER WARNING: The original Java variable was marked 'final':
            //ORIGINAL LINE: final int lowLength = Math.Min(coefficients.length, p.coefficients.length);
            int lowLength = Math.Min(coefficients.Length, p.coefficients.Length);
            //JAVA TO C# CONVERTER WARNING: The original Java variable was marked 'final':
            //ORIGINAL LINE: final int highLength = Math.Max(coefficients.length, p.coefficients.length);
            int highLength = Math.Max(coefficients.Length, p.coefficients.Length);

            // build the coefficients array
            double[] newCoefficients = new double[highLength];
            for (int i = 0; i < lowLength; ++i)
            {
                newCoefficients[i] = coefficients[i] + p.coefficients[i];
            }
            Array.Copy((coefficients.Length < p.coefficients.Length) ? p.coefficients : coefficients, lowLength, newCoefficients, lowLength, highLength - lowLength);

            return new PolynomialFunction(newCoefficients);

        }
        :return:
        """

        if len(self.coefficients) >= len(p.coefficients):
            lowLength = p.coefficients
            highLength = self.coefficients
        else:
            highLength = p.coefficients
            lowLength = self.coefficients

        newCoefficients = []
        for i in range(lowLength):
            newCoefficients[i] = self.coefficients[i] + p.coefficients[i]

        if len(self.coefficients) >= len(p.coefficients):
            tempCoefficients = self.coefficients[lowLength:]
            newCoefficients = newCoefficients + tempCoefficients
        else:
            tempCoefficients = p.coefficients[lowLength:]
            newCoefficients = newCoefficients + tempCoefficients
        return PolynomialFunction(newCoefficients)

    def subtract(self, p):
        """
        public virtual PolynomialFunction subtract(PolynomialFunction p)
        {

            // identify the lowest degree polynomial
            int lowLength = Math.Min(coefficients.Length, p.coefficients.Length);
            int highLength = Math.Max(coefficients.Length, p.coefficients.Length);

            // build the coefficients array
            double[] newCoefficients = new double[highLength];
            for (int i = 0; i < lowLength; ++i)
            {
                newCoefficients[i] = coefficients[i] - p.coefficients[i];
            }
            if (coefficients.Length < p.coefficients.Length)
            {
                for (int i = lowLength; i < highLength; ++i)
                {
                    newCoefficients[i] = -p.coefficients[i];
                }
            }
            else
            {
                Array.Copy(coefficients, lowLength, newCoefficients, lowLength, highLength - lowLength);
            }

            return new PolynomialFunction(newCoefficients);

        }
        :return:
        """
        if len(self.coefficients) >= len(p.coefficients):
            lowLength = p.coefficients
            highLength = self.coefficients
        else:
            highLength = p.coefficients
            lowLength = self.coefficients

        newCoefficients = []
        for i in range(lowLength):
            newCoefficients[i] = self.coefficients[i] - p.coefficients[i]

        if len(self.coefficients) < len(p.coefficients):
            for i in range(lowLength, highLength):
                newCoefficients[i] = -p.coefficients[i]
        else:
            newCoefficients = newCoefficients + self.coefficients[lowLength:]

        return PolynomialFunction(newCoefficients)

    def negate(self):
        """
        public virtual PolynomialFunction negate()
        {
            double[] newCoefficients = new double[coefficients.Length];
            for (int i = 0; i < coefficients.Length; ++i)
            {
                newCoefficients[i] = -coefficients[i];
            }
            return new PolynomialFunction(newCoefficients);
        }
        :return:
        """
        newCoefficients = []
        for i in range(len(self.coefficients)):
            newCoefficients = -self.coefficients[i]
        return PolynomialFunction(newCoefficients)

    def multiply(self, p):
        """
        public virtual PolynomialFunction multiply(PolynomialFunction p)
        {

            double[] newCoefficients = new double[coefficients.Length + p.coefficients.Length - 1];

            for (int i = 0; i < newCoefficients.Length; ++i)
            {
                newCoefficients[i] = 0.0;
                for (int j = Math.Max(0, i + 1 - p.coefficients.Length); j < Math.Min(coefficients.Length, i + 1); ++j)
                {
                    newCoefficients[i] += coefficients[j] * p.coefficients[i - j];
                }
            }

            return new PolynomialFunction(newCoefficients);
        :return:
        """
        newCoefficients = []
        for i in range(len(self.coefficients)):
            newCoefficients[i] = 0.0
            start = i + 1 - len(p.coefficients)
            stop = len(self.coefficients)
            if 0 > start:
                start = 0

            if stop > i + 1:
                stop = i + 1

            for j in range(start, stop):
                newCoefficients[i] += self.coefficients[j] * p.coefficients[i - j]

            return PolynomialFunction(newCoefficients)

    @staticmethod
    def differentiate(coeff):
        """
        protected internal static double[] differentiate(double[] coeff)
            {
                int n = coeff.Length;
                if (n == 0)
                {
                    throw new ArgumentNullException("coeff is null");
                }
                if (n == 1)
                {
                    return new double[] { 0 };
                }
                double[] result = new double[n - 1];
                for (int i = n - 1; i > 0; i--)
                {
                    result[i - 1] = i * coeff[i];
                }
                return result;
            }
        """
        n = len(coeff)
        if n == 0:
            raise ArgumentsException("coeff is null")
        if n == 1:
            return [0]
        result = [0] * (n - 1)
        for i in range(n - 1, 1, -1):
            result[i - 1] = i * coeff[i]
        return result

    def polynomialDerivative(self):
        return PolynomialFunction(self.differentiate(self.coefficients))

    def derivative(self):
        return self.polynomialDerivative()


if __name__ == '__main__':
    a = PolynomialFunction.differentiate([1, 2, 3])
    print a
