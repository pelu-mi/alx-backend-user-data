#!/usr/bin/env python3
""" Module to implement methods handling personal data
"""

from typing import List
import re


def filter_datum(fields: List, redaction: str,
                 message: str, separator: str) -> str:
    """ Return the log message obfuscated
    """
    records: List = message.split(separator)
    for i in range(len(records)):
        for field in fields:
            records[i] = re.sub(field + ".*", field + "=xxx", records[i])
    return separator.join(records)
