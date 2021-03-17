#!/usr/bin/env python

rh = {
    "username": "",
    "password": "",
}

config = {
    "statusEmailAddress": "3.14159.rice@gmail.com",
    "buyLimit": 0.0075,
    "sellLimit": 0.02,
    "movingAverageWindows": 24,    # 4 hours * 6 samples per hour
    "runMinute": [5,15,25,35,45,55],
    "coinList": ["ETC"],
    "tradesEnabled": False,
    "rsiWindow": 48,
}
