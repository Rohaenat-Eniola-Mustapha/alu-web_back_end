#!/usr/bin/env python3
"""
First File
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination
    parameters.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index
        and end index for the items on the page.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
