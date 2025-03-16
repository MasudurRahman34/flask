from flask import Flask, render_template, request
from Maths.mathematics import *
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result=summation(num1,num2)
    return str(result)
    # Write your code here

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result=subtraction(num1,num2)
    return str(result)
    # Write your code here

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result=multiplication(num1,num2)
    
    # Write your code here  

@app.route("/")
def render_index_page():
    return render_template("index.html")
    # Write your code here
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
