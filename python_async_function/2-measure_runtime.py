#!/usr/bin/env python3

"""
Module containing the async routine `measure_time`
"""

import asyncio
import random
from typing import Callable
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
     Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per coroutine.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average runtime per coroutine.
    """

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = start_time - end_time
    return total_time / n
