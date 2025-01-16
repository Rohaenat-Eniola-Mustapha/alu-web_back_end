#!/usr/bin/env python3
"""
Module that returns log message
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with sensitive fields to redact.

        Args:
            fields (List[str]): The fields to be redacted.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by redacting sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with sensitive fields redacted.
        """
        original_message = super().format(record)
        return filter_datum(self.fields, 
                            self.REDACTION, 
                            original_message, 
                            self.SEPARATOR)

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
