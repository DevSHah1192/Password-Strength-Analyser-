from flask import Flask, render_template, request

app = Flask(__name__)


def check_password(password):

    points = 0
    missing = []

    # Length check
    if len(password) >= 8:
        points += 1
    else:
        missing.append("At least 8 characters")

    # Uppercase check
    has_upper = False
    for ch in password:
        if ch.isupper():
            has_upper = True
            break

    if has_upper:
        points += 1
    else:
        missing.append("At least one uppercase letter")

    # Lowercase check
    has_lower = False
    for ch in password:
        if ch.islower():
            has_lower = True
            break

    if has_lower:
        points += 1
    else:
        missing.append("At least one lowercase letter")

    # Digit check
    has_digit = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
            break

    if has_digit:
        points += 1
    else:
        missing.append("At least one digit")

    # Special character check
    special_chars = "@#$^&*"
    has_special = False
    for ch in password:
        if ch in special_chars:
            has_special = True
            break

    if has_special:
        points += 1
    else:
        missing.append("At least one special character (@#$^&*)")

    if points <= 2:
       strength = "Weak"
    elif points <= 4:
        strength = "Medium"
    else:
      strength = "Strong"

    return strength, points, missing


@app.route("/", methods=["GET", "POST"])
def home():
    result = {}

    if request.method == "POST":
        password = request.form["password"]
        strength, points, missing = check_password(password)

        result = {
            "strength": strength,
            "points": points,
            "missing": missing
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
