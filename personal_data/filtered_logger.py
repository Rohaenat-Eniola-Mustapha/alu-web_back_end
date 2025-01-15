#!/usr/bin/env python3
"""
Module that returns log message
"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Function that returns the log message
    obfuscated.

    Args:
        fields (List): a list of strings representing all fields to obfuscate.
        redaction (str): a string representing...
        message (str): a string representing the log line
        separator (str): a string representing...

    Returns:
        String: The log message obfuscated.
    """
    pattern = f"({'|'.join(map(re.escape, fields))})=.*?(?={separator}|$)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
