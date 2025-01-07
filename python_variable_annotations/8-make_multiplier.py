#!/usr/bin/env python3

"""
Module for a type-annotated function make_multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns the function that multiplies a float 
    by multiplier"""
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
