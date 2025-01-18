#!/usr/bin/env python3
"""
Module that Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password with a salt using bcrypt.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates that the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain text password to validate.

    Returns:
        bool: True if the password matches the hash, False otherwise.
    """
    if not isinstance(hashed_password, bytes):
        raise TypeError("Hashed password must be of type bytes")
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    # Use bcrypt to check if the password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
