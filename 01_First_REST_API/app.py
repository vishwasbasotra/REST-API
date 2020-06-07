# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 01:32:58 2020

@author: Vishwas Basotra
"""
# importing flask

from flask import Flask

app = Flask(__name__)

@app.route('/')    #http://www.google.com/
def home():
    return "hello world"

app.run(port=5000)
