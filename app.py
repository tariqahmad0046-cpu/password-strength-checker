from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search("[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search("[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search("[0-9]", password):
        strength += 1
    else:
        feedback.append("Add numbers")

    if re.search("[@#$%^&+=!]", password):
        strength += 1
    else:
        feedback.append("Add special characters")

    if strength <= 2:
        return "Weak", feedback
    elif strength <= 4:
        return "Medium", feedback
    else:
        return "Strong", feedback

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    feedback = []
    
    if request.method == "POST":
        password = request.form["password"]
        result, feedback = check_password_strength(password)

    return render_template("index.html", result=result, feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
