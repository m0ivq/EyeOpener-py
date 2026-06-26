from flask import Flask

from poc_routes import poc_bp
from main_routes import main_bp

app = Flask(__name__)

app.register_blueprint(poc_bp)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)