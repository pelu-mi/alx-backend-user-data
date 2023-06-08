#!/usr/bin/env python3
""" Module to implement methods handling personal data
"""

import re
import mysql
import logging
from os import environ
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Return the log message obfuscated
    """
    for f in fields:
        message = re.sub("{}=.*?{}".format(f, separator),
                         "{}={}{}".format(f, redaction, separator), message)
    return message


def get_logger() -> logging.Logger:
    """ Return a Logger object for logging
    """
    # Create Logger
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logging.propagate = False
    # Create Stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Get info from mysql db
    """
    user = environ.get('PERSONAL_DATA_DB_USERNAME')
    pwd = environ.get('PERSONAL_DATA_DB_PASSWORD')
    host = environ.get('PERSONAL_DATA_DB_HOST')
    db_name = environ.get('PERSONAL_DATA_DB_NAME')
    # MySQL connection object
    cnx = mysql.connector.connection.MySQLConnection(user=user,
                                                     password=pwd,
                                                     host=host,
                                                     database=db_name)
    return cnx


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format string based on format and filter_datum
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
