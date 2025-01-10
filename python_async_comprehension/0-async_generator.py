#!/usr/bin/env python3

import asyncio
import random
from typing import Generator

"""Module containing async_generator function"""


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous coroutine will loop 10 times,
    wait 1 second, then yield a random number between
    0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
