from flask import Flask, Response, request, session, url_for, redirect

# Creating Student Form
std_form = Flask(__name__)
std_form.secret_key = "supersecreate"  # Required to use sessions

@std_form.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        std_first_name = request.form.get("student_name")
        std_middele_name = request.form.get("student_middle")
        std_last_name = request.form.get("student_last")

        if (std_first_name == "Vishal" and std_middele_name == "Sadanand" and std_last_name == "Gaikwad"):
            session['user'] = f"{std_first_name} {std_middele_name} {std_last_name}"
            return redirect(url_for("welcome"))
        else:
            return '''
                <h2>Invalid Credentials. Try Again!</h2>
                <form action="/" method="get">
                    <button type="submit">Back to Login</button>
                </form>
            '''

    return '''
        <h2>Hello Student, Please Fill Your Form</h2>   
        <form method="POST">
            Student First Name: <input type="text" placeholder="Enter First name" name="student_name"><br>
            Student Middle Name: <input type="text" placeholder="Enter Middle name" name="student_middle"><br>
            Student Last Name: <input type="text" placeholder="Enter Last name" name="student_last"><br>
            <input type="submit" value="login">
        </form>
    '''

@std_form.route("/Welcome")
def welcome():
    if 'user' in session:
        return f'''
        
        <h2>Hello {session['user']}, welcome to this college website!</h2>
        <input type="submit" value="Go Back">
        <a href="{url_for('home')}">Go to Home Page</a>
        
        '''
    else:
        return redirect(url_for("home"))

if __name__ == '__main__':
    std_form.run(debug=True)
