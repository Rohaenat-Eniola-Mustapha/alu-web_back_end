#!/usr/bin/env python3

"""
Module containing an asynchronous coroutine 'wait_random'.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum number of seconds
        to wait (default: 10).

    Returns:
        float: The actual delay time.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay