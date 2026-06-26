from flask import Blueprint, render_template

poc_bp = Blueprint("poc", __name__)

@poc_bp.route("/poc")
def poc():
    return render_template("poc_index.html")

@poc_bp.route("/poc/control")
def poc_control():
    return render_template("poc_control.html")