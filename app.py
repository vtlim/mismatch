import sys
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('main.html')

@app.route('/', methods=['GET', 'POST'])
def my_form_post():

    if request.method == 'GET':
        return render_template('main.html')

    # if request is post
    form_data = request.form
    print("the LHS text is: ", form_data["text_lhs"])
    print("the RHS text is: ", form_data["text_rhs"])
    result = ""
    return render_template('main.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
