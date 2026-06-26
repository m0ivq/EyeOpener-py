from flask import Blueprint, request, jsonify

main_bp = Blueprint("main", __name__)

scene = {
    "right_x": 0.0,
    "right_y": 0.0,
    "left_brightness": 1.0,
    "right_brightness": 1.0,
}

@main_bp.route("/api/state", methods=["GET", "POST"])
def api_state():
    print(request.method, request.remote_addr, request.user_agent)
    global scene

    if request.method == "POST":
        data = request.json or {}

        for key in scene:
            if key in data:
                scene[key] = float(data[key])

    return jsonify(scene)