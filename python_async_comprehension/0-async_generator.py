#!/usr/bin/env python3

import asyncio
import random

"""Module containing async_generator function"""


async def async_generator():
    """
    Asynchronous coroutine will loop 10 times,
    wait 1 second, then yield a random number between
    0 and 10.
    """
    for i in range(10):
        yield i
        await asyncio.sleep(1)
