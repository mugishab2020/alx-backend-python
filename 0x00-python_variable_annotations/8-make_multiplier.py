#!/usr/bin/env python3
'''his is the task to return the function'''


from typing import Callable, List


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''we are making the inner function to return'''

    def multiply(multi: float):
        return multiplier * multi
    return multiply
