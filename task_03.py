#!/usr/bin/env python
#! -*- coding: utf-8 -*-

""" A really good docstring of task 03"""

import decimal

NAME = raw_input ('What is your name?' )

STARTING_AMOUNT = raw_input('what is the amount of your principal')
STARTING_AMOUNT = int(STARTING_AMOUNT)

YEARS = raw_input ('for how many years is this loan beaing borrowed?')
YEARS = int(YEARS)

PRE_QUALIFIED = raw_input ('are you pre-qualified for this loan?')

STATUS = PRE_QUALIFIED[:1].lower() == 'y'
ANSWER = 'yes'
TOTAL = 0
RATE = 0

if STARTING_AMOUNT <= 199999:
    if 1 <= YEARS <=15:
        if STATUS:
            RATE = decimal.Decimal(3.63)/100
        else:
            RATE = decimal.Decimal (4.65) / 100
            ANSWER = 'no'

    elif 16 <= YEARS <= 20:
        if STATUS:
            RATE = decimal.Decimal(4.04)/100
        else:
            RATE = decimal.Decimal (4.04)/100
            ANSWER = 'no'
elif 200000 <= STARTING_AMOUNT <+ 999999:
    if 1 <= YEARS <= 15:
        if STATUS:
            RATE = decimal.Decimal (3.02) / 100
        else:
            RATE = decimal.Decimal (3.98) /100
            ANSWER ='no'
    elif 16 <= YEARS <= 20:
        if STATUS:
            RATE = decimal.Decimal(3.27)/100
        else:
            RATE = decimal.Decimal(4.08)/100
            ANSWER = 'no'
    elif 21 <= YEARS <= 30:
        if STATUS:
            RATE = decimal.Decimal(4.66) / 100
        else:
            RATE is None
            ANSWER = 'No'

else:
    if 1 <= YEARS <= 15:
        if STATUS:
            RATE = decimal.Decimal(2.05) / 100
        else:
            RATE = 0
            ANSWER = 'no'
    elif 16 <= YEARS <= 20:
        if STATUS:
            RATE = decimal.Decimal(2.62)/100
        else:
            RATE is None
            ANSWER = 'no'

    else:
        if STATUS:
            RATE is None
        else:
            RATE is None
            ANSWER = 'No'
        if not STATUS:
            ANSWER = 'No'

if RATE is None:
    TOTAL = None
else:
    TOTAL = int(
        round(STARTING_AMOUNT * ((1+ (RATE/12))
                                 ** (12 * YEARS))))

OUTCOME = ('loan total is: {:>35}'
           'principal: ${:>40,.0f}'
           'years: {:>39}yaers'
           'Pre-Qualified?: {:>36}'
           'Total: ${:>44,.0f}')

print OUTCOME.format(NAME, STARTING_AMOUNT, YEARS, ANWER, TOTAL)




