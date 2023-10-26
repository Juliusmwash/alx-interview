#!/usr/bin/python3
"""Determines a valid UTF-8 encoding"""


def validUTF8(data):
    """
    bit_check1 checks if significant bit is 1
    bit_check2 checks if second significant bit is 0
    track - keeps track of how many 1s occurs before 0
    data - a list of integers to check
    """

    bit_check1 = 1 << 7
    bit_check2 = 1 << 6
    track = 0

    if not data or len(data) == 0:
        return True

    for num in data:
        bit = 1 << 7
        if track == 0:
            while (bit & num):
                track += 1
                bit = bit >> 1

            if track == 0:
                continue
            if track == 1 or track > 4:
                return False
        else:

            if not (num & bit_check1 and not (num & bit_check2)):
                return False
        track -= 1

    if track:
        return False
    else:
        return True
