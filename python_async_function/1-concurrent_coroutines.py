#!/usr/bin/env python3

"""
Module containing the async routine `wait_n`.
"""

import asyncio
from typing import List
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `wait_random` n times
    with the specified max_delay and returns a list of all delays
    in ascending order without using `sort()`.

    Args:
        n (int): Number of times to spawn `wait_random`.
        max_delay (int): Maximum delay value for each `wait_random`.

    Returns:
        List[float]: List of delays in ascending order.
    """

    task = [wait_random(max_delay) for i in range(n)]
    delay = []
    for task in asyncio.as_completed(task):
        result = await task
        delay.append(result)
    return delay
