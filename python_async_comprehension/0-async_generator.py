#!/usr/bin/env python3
"""
Module containing async_generator function
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:  # type: ignore
    """
    Asynchronous coroutine will loop 10 times,
    wait 1 second, then yield a random number between
    0 and 10.

    Args:
        None

    Returns:
        Float: The loop that will be generated when
        a random number is yielded will be a float.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
