import os
import subprocess
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]

        if file:
            input_path = os.path.join(UPLOAD_FOLDER, file.filename)
            output_path = os.path.join(OUTPUT_FOLDER, "obf_" + file.filename)

            file.save(input_path)

            command = [
                "lua5.1",
                "./Prometheus/cli.lua",
                "--preset", "Medium",
                input_path,
                "--output",
                output_path
            ]

            subprocess.run(command)

            return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
