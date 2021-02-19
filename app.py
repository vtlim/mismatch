import sys
import flask

app = flask.Flask(__name__)

def reverse_complement(sequence):
    """
    """
    base_orig = ("U", "A", "T", "C", "G", "X", "Y")
    base_rev = ("T", "X", "A", "Y", "C", "T", "G")
    revcomp = sequence[::-1]
    for orig, rev in zip(base_orig, base_rev):
        revcomp = revcomp.replace(orig, rev)
    return revcomp

def locate_difference(text1, text2):
    """
    """
    # https://stackoverflow.com/a/8545568
    where_diff = [i for i in range(len(text1)) if text1[i] != text2[i]]
    return where_diff

# -------------------------------------------------------------------------

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/process_sequences')
def process_sequences():

    # get raw string from each side
    raw_lhs = flask.request.args.get('text_lhs')
    raw_rhs = flask.request.args.get('text_rhs')

    # split raw string into list for processing
    list_lhs = raw_lhs.split("\n")
    list_rhs = raw_rhs.split("\n")
    if len(list_lhs) != len(list_rhs):
        return flask.jsonify({
            "result_error": "ERROR: Please enter the same number of lines in both text boxes.",
        })

    # determine reverse complement and identify mismatch
    master_index_list = []
    master_lhs = []
    master_rhs = []
    last_len = 0
    for i, (item_lhs, item_rhs) in enumerate(zip(list_lhs, list_rhs)):

        # strip any spaces or commas, capitalize, check lengths
        seq_lhs = item_lhs.strip(" ,").upper()
        seq_rhs = item_rhs.strip(" ,").upper()
        if len(seq_lhs) != len(seq_rhs):
            return flask.jsonify({
                "result_error": f"ERROR: Please check that line {i+1} is the same length in both text boxes.",
            })

        # take reverse complement and find mismatches
        revcomp_rhs = reverse_complement(seq_rhs)
        index_list = locate_difference(seq_lhs, revcomp_rhs)
        adjusted_index_list = [x+last_len for x in index_list]

        # add offset for next line's highlighting, add 5 for <br/>
        last_len += len(seq_lhs)
        last_len += 5

        # store and move on
        master_index_list.append(adjusted_index_list)
        master_lhs.append(seq_lhs)
        master_rhs.append(revcomp_rhs)

    # flatten the index list from 2d to 1d
    master_index_list = [item for sublist in master_index_list for item in sublist]

    # join list back to string
    result_lhs = "<br/>".join(master_lhs)
    result_rhs = "<br/>".join(master_rhs)

    return flask.jsonify({
        "result_lhs": result_lhs,
        "result_rhs": result_rhs,
        "indexList": master_index_list,
        "result_error": "",
    })

    return flask.jsonify({
        "result_lhs": result_lhs+"!",
        "result_rhs": result_rhs+"!",
        "indexList": [0,2,4],
        "result_error": "TEST",
    })

@app.route('/about')
def about():
    return flask.render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
