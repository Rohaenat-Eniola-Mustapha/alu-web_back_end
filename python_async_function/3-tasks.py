#!/usr/bin/env python3
"""
Module containing the task_wait_random function.
"""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that executes the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for wait_random.

    Returns:
        asyncio.Task: An asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
