"""Subtraction Class"""
import pprint
import operator

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        result = self.values[0]
        for n in self.values[1:]:
            result -= n
        return result
