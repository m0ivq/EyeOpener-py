from flask import Flask
import subprocess
import os

from poc_routes import poc_bp
from main_routes import main_bp


ADB_PATH = r"C:\tools\platform-tools\adb.exe"
PORT = 5000


def setup_adb():
    """Automatically configure ADB reverse if a Quest is connected."""

    if not os.path.exists(ADB_PATH):
        print(f"[ADB] Not found: {ADB_PATH}")
        return

    try:
        # Check connected devices
        result = subprocess.run(
            [ADB_PATH, "devices"],
            capture_output=True,
            text=True,
            check=True
        )

        devices = [
            line for line in result.stdout.splitlines()
            if "\tdevice" in line
        ]

        if not devices:
            print("[ADB] No authorised Quest detected.")
            return

        print(f"[ADB] Quest detected: {devices[0].split()[0]}")

        # Configure reverse port forwarding
        subprocess.run(
            [
                ADB_PATH,
                "reverse",
                f"tcp:{PORT}",
                f"tcp:{PORT}"
            ],
            check=True,
            capture_output=True,
            text=True
        )

        print(f"[ADB] Reverse tcp:{PORT} -> tcp:{PORT} configured.")

    except subprocess.CalledProcessError as e:
        print(f"[ADB] Error:\n{e.stderr}")


app = Flask(__name__)

app.register_blueprint(poc_bp)
app.register_blueprint(main_bp)


if __name__ == "__main__":
    print("===================================")
    print(" EyeOpener")
    print("===================================")

    setup_adb()

    print(f"[Flask] Starting on http://127.0.0.1:{PORT}")

    app.run(
        host="127.0.0.1",
        port=PORT,
        debug=True
    )