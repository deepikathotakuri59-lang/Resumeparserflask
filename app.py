from flask import Flask, render_template, request
import os
import pdfplumber

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = ""

    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return f"<h2>Resume Text</h2><pre>{text}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
import os
