from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="rot">Rotate by:</label>
            <input name="rot" value="0" type="text">
            <textarea name="text">{0}</textarea>
            <input value="Submit Query" type="submit">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["POST"])
def encrypt():
    user_input = str(request.form["text"])
    rot_number = int(request.form["rot"])
    answer = rotate_string(user_input, rot_number)
    return "<h1" + form.format(answer) + "</h1>"

app.run()