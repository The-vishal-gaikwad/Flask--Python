from flask import request, Flask, Response, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "VISHALDJ"  # Required to use sessions

#Route: Login Page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "Admin" and password == "123":
            session['user'] = username  # Save user in session
            return redirect(url_for("welcome"))  # Redirect to welcome page
        else:
            return  '''
                <h2>Invalid Credentials. Try Again!</h2>
                <form action="/" method="get">
                    <button type="submit">Back to Login</button>
                </form>
            '''
    # If GET request, show the login form
    return '''
        <h2>Login Page</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

#Route: Welcome Page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome,{session["user"]}!</h2>
            <a href="{url_for('logout')}">Logout</a>
        '''
    else:
        return redirect(url_for("login"))

#Route: Logout
@app.route("/logout")
def logout():
    session.pop("user", None)  # Remove user from session
    return redirect(url_for("login"))  # Redirect to login page

#Run the app
if __name__ == '__main__':
    app.run(debug=True)




