#!/usr/bin/env python3
""" doc """

import random
from typing import Any

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[Any]:
    """ doc """
    return [i async for i in async_generator()]
