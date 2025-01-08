#!/usr/bin/env python3
"""
Module containing the measure_time function.
"""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per coroutine.

    Args:
        n (int): Number of coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average runtime per coroutine.
    """
    start_time = time.perf_counter()  # Start the timer
    asyncio.run(wait_n(n, max_delay))  # Run the asynchronous function
    end_time = time.perf_counter()  # End the timer

    total_time = end_time - start_time
    return total_time / n
