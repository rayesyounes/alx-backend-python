#!/usr/bin/env python3
""" doc """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ doc """
    sum = 0
    for i in input_list:
        if type(i) == float:
            sum += i
    return sum
