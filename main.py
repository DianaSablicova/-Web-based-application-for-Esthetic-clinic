from flask import Flask, render_template, redirect, request,  session, jsonify, url_for, flash
from flask_session import Session
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
import re

from helpers import login_required, apology



app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app = Flask(__name__, static_url_path='/static')
db = SQL("sqlite:///mydatabasename.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not email or not password:
             return apology("Email and password required")
        elif not email:
            return apology("Email required")
        elif not password:
            return apology("Password required")
        elif not confirmation:
             return apology("Confirmation of password required")
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return apology("Wrong email adress")
        elif password != confirmation:
             return apology("Password and confirmation do not match")
        elif len(rows) == 1 :
             return apology("This email has been already registered")
        else:
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users (email, hash) VALUES (?, ?)", email, hash)
            return render_template("login.html")

    else:
        return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    msg = " "
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("email"):
            return apology("Must provide email")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            msg = "invalid username and/or password"
            return msg

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route('/treatments')
def treatments():
    return render_template('treatments.html')


@app.route('/prising')
def prising():
    return render_template('prising.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/return-homepage')
def returno():
    return render_template('return-homepage.html')

@app.route('/personal')
def personal():
    return render_template('personal.html')




@app.route("/booking", methods=['GET', 'POST'])
@login_required
def booking():
    selected_date = request.args.get('date')
    if selected_date:
        # Query the database to get the appointments for the selected date
        appointments = db.execute("SELECT time FROM appointments WHERE date = ?", selected_date)
        # Extract the times from the query result
        booked_times = [appointment['time'] for appointment in appointments]

        return render_template("booking.html", selected_date=selected_date, booked_times=booked_times)
    return render_template("booking.html")



@app.route('/book', methods=['POST'])
def book():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        treatments = request.form.get('treatments')
        time = request.form.get('time')

        if "user_id" in session:
            user_id = session["user_id"]
            # Query the database to get the user's email
            user = db.execute("SELECT email FROM users WHERE id = ?", user_id)
            if user:
                email = user[0]["email"]
            else:
                # Handle the case where the user's email is not available
                return jsonify({"success": False, "message": "User not authenticated."})
        else:
            # Handle the case where the user is not logged in
            return jsonify({"success": False, "message": "User not authenticated."})

        # Check if the selected time slot is available
    existing_appointments = db.execute("SELECT * FROM appointments WHERE date = ? AND time = ?", date, time)

    if len(existing_appointments) > 0:
        # Time slot is already booked, show a message and redirect to the booking page
        flash("The selected time slot is not available.", "danger")
        return redirect(url_for('booking'))
    elif len(existing_appointments) == 0:
        # Time slot is available, insert the appointment into the database
        db.execute("INSERT INTO appointments (name, email, date, time, treatments) VALUES (?, ?, ?, ?, ?)", name, email, date, time, treatments)
        # Show a success message and redirect to the homepage
        flash("Appointment booked successfully!", "success")
        return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run()