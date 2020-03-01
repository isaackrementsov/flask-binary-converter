# Isaac Krementsov
# 3/1/2020
# Introduction to Systems Engineering
# Flask Binary Converter - Flask app to convert binary numbers to decimals

from flask import Flask, render_template, request
import json

app = Flask(__name__)


# Method to convert a binary number as a string to a decimal
def to_decimal(binary):

    # Separate the parts of the number that are less than or greater than 2^0, ex. 10.1 -> [10, 1]
    parts = binary.split('.')

    # The first part of the split binary will be positive powers of two
    pos_powers = parts[0][::-1] # The string should be reversed so that the powers of 2 are ascending (x*2^0 + y*2^1 + ...)

    # This is the decimal number that will be the end result of the conversion
    decimal = 0.0

    # Loop through the positive powers; A for-loop is not used here because we need to keep track of the index
    p = 0
    while(p < len(pos_powers)):
        binary_digit = int(pos_powers[p]) # Get the value of each individual digit, which is 1 or 0
        decimal += binary_digit * 2**p # Add 2 to the power of the digit and multiplied by the digit to convert it to a decimal value

        p += 1

    # If there is a component of the binary number where there are digits below 2^0, add this component
    if(len(parts) > 1):
        # The negative powers are after the "." in the original binary string
        neg_powers = parts[1][::-1] # These are also reversed, so that the powers increase in magnitude

        # Loop through and add on the negative powers
        n = 0
        while(n < len(neg_powers)):
            binary_digit = int(neg_powers[n])
            decimal += binary_digit * 2**(-(n + 1)) # Add 2^-(n + 1), so that the digits are 2^-1, 2^-2, ...

            n += 1

    # Once all of the binary values are added on, return the decimal result
    return decimal


@app.route('/', methods=['GET'])
def home():
    return render_template('binaryconverter.html')

@app.route('/convert_binary', methods=['GET'])
def convert_binary():
    binary_string = request.values['binary_string']
    return json.dumps(to_decimal(binary_string))
