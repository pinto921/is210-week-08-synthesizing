#!/ usr/bin/en python
# -*- coding: utf-8 -*-

""" task 2"""

DAY = raw_input( 'welcome user, what day it is').lower()[:3:]
TIME = raw_input(' what time is it?') [:4:]
TIME = int(TIME)

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < 0600 else False

if SNOOZE == False:
    print 'Beep! Beep! Beep! Beep!'

    
