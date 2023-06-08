#!/usr/bin/env python3
""" Module to implement methods handling personal data
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Return the log message obfuscated
    """
    for f in fields:
        message = re.sub("{}=.*?{}".format(f, separator), 
                         "{}={}{}".format(f, redaction, separator), message)
    return message
