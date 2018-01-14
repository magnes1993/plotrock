from flask import Flask
from flask import jsonify

app = Flask(__name__)


def read_file(file_name):
    with open(file_name, "r") as html_file:
        return html_file.read()
    return ""


@app.route("/web")
def web():
    return read_file("assets/simple_chart.html")


@app.route('/js/<file>')
def static_content(file):
    return read_file("assets/"+file)


@app.route("/alg/sensitivity")
def sensitivity():
    return jsonify({
        "cols": [
            {"id":"","label":"Topping","pattern":"","type":"string"},
            {"id":"","label":"Slices","pattern":"","type":"number"}
        ],
        "rows": [
            {"c":[{"v":"Mushrooms", "f": None}, {"v":3,"f":None}]},
            {"c":[{"v":"Onions", "f": None}, {"v":1,"f":None}]},
            {"c":[{"v":"Olives", "f": None}, {"v":1,"f":None}]},
            {"c":[{"v":"Zucchini", "f": None}, {"v":1,"f":None}]},
            {"c":[{"v":"Pepperoni", "f": None}, {"v":2,"f":None}]}
        ]
    })


if __name__ == "__main__":
    app.run()
