#!/usr/bin/env python3
import sys
import subprocess
from flask import Flask, request
app = Flask(__name__)

def FindSpecial(pw, special_chars):
    for c in special_chars:
        if (c in pw):
            return True

def FindDigit(pw, digits):
    for c in digits:
        if (c in pw):
            return True

@app.route('/')
def generate_password():
    nw = request.args.get('nw')
    ns = request.args.get('ns')

    if (int(ns) < 2):
        result = subprocess.check_output("diceware -n {NW} -s {NS}".format(NW = nw, NS = ns), stderr=subprocess.STDOUT, shell=True)
        result = result.decode("UTF8").strip()
        return result

    special_chars = "!#%/()=?@£$€{[]}\\+*.:,;|"
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(100):
        result = subprocess.check_output("diceware -n {NW} -s {NS}".format(NW = nw, NS = ns), stderr=subprocess.STDOUT, shell=True)
        result = result.decode("UTF8").strip()
        if (FindDigit(result, digits) and FindSpecial(result, special_chars)):
            return result

if __name__ == "__main__":
    app.run()
