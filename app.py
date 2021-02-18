import sys
import flask

app = flask.Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('main.html')

@app.route('/process_sequences')
def process_sequences():

    #form_data = request.form
    #seqs_lhs = form_data["text_lhs"].split("\n")
    #seqs_rhs = form_data["text_rhs"].split("\n")
    #print("the LHS text is: ", seqs_lhs)
    #print("the RHS text is: ", seqs_rhs)
    #result = ""
    #return render_template('main.html', result=result)
    a = int(flask.request.args.get('text_lhs'))
    b = int(flask.request.args.get('text_rhs'))
    return flask.jsonify({"result_lhs": a+1, "result_rhs":b+1})


if __name__ == "__main__":
    app.run(debug=True)
