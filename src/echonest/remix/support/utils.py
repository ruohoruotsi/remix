#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

Utility functions, esp needed during porting from 2.7 to 3.5
"""

def strlit2bytes(str):
    return bytes(str, 'utf-8')