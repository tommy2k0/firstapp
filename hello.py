# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:40:14 2017

@author: Lenovo
"""

from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=5000, debug=True)