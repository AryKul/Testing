#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:51:32 2022

Decoration

https://www.youtube.com/watch?v=tuFuDKE7DF8&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa&index=20

@author: ary
"""
import webbrowser


def validator(func): # 1 param = func. Here func - open_url
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Wrong URL")
    return wrapper


@validator # run something =  wrapper before func = open_url
def open_url(url):
    webbrowser.open(url)

open_url("https://itprogercom/course/python/20")
open_url("https://itproger.com/course/python/20")

# Testing
