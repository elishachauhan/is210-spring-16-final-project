#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for PriceLife"""

import stores

WELCOME = 'Welcome to PriceLife'
BEGIN = 'Are you looking for a good price? (y/n)'
ITEM = 'Which item are you looking for?'
STORE = 'Do you prefer an alert? (y/n)'
END = 'Are you finished? (y/n)'
SALUTATION = 'Thank you and good bye.'


def startup():
    """
    Args:

    Returns:

    Examples:
        >>>
    """
    print WELCOME
    price = raw_input(BEGIN)
    item = raw_input(ITEM)
    alert = raw_input(STORE)
    if alert is 'y':
        raw_input(END)
    else:
        raw_input(SALUTATION)

startup()
