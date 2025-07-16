from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("welcome.html")

@app.route("/login", methods=["POST"])
def Login_student():
    Username = request.form.get("username")
    Password = request.form.get("password")

    pass_dict = {
        'vishal': '123',
        'admin': 'pass',
    }

    if Username in pass_dict and pass_dict[Username] == Password:
        return render_template("entry.html", user=Username)
    else:
        return "Invalid username or password"

if __name__ == '__main__':
    app.run(debug=True)
