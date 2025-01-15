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
        redaction (str): a string representing by what the field will be obfuscated.
        message (str): a string representing the log line
        separator (str): a string representing by which character is separating all fields in the log line (message)

    Returns:
        String: The log message obfuscated.
    """
    pattern = f"({'|'.join(map(re.escape, fields))})=.*?(?={separator}|$)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
