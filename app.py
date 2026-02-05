from flask import Flask, render_template, request
from model import check_spelling

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    original_text = ""
    corrected_text = ""
    corrections = {}

    if request.method == "POST":
        original_text = request.form.get("text", "")
        corrected_text, corrections = check_spelling(original_text)

    return render_template(
        "index.html",
        original_text=original_text,
        corrected_text=corrected_text,
        corrections=corrections
    )

if __name__ == "__main__":
    app.run(debug=True)