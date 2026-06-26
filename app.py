from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

state = {
    "right_x": 0.0,
    "right_y": 0.0,
    "left_brightness": 1.0,
    "right_brightness": 1.0,
}

@app.route("/poc")
def poc():
    return render_template("poc_index.html")

@app.route("/poc/control")
def poc_control():
    return render_template("poc_control.html")

@app.route("/api/state", methods=["GET", "POST"])
def api_state():
    global state

    if request.method == "POST":
        data = request.json or {}
        for key in state:
            if key in data:
                state[key] = float(data[key])

    return jsonify(state)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)