#!/usr/bin/env python3
""" doc """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ doc """
    tasks = []
    delays = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: delays.append(x.result()))
        tasks.append(task)
    await asyncio.gather(*tasks)
    return delays
