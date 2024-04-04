#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:number>')
def count(number):
    numbers = range(number +1)
    return '<br>'.join(map(str, numbers))
    
@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result =None
    if operation == '+':
        result == num1+num2
    elif operation == '*':
        result == num1*num2
    elif operation == '-':
        result == num1-num2 
    elif operation == '*/':
        if num2!=0:
            result == num1/num2 
    elif operation == '%':
        result == num1%num2  

    if result is not None:
        return str(result)
    else:
        return 'Invalid operation!'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
