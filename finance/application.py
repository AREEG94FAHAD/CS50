import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    cash=db.execute("select cash from users where id=:id",id=session["user_id"])
    v=cash[0]["cash"]

    b=db.execute("select symbol , sum(shares) as totalsymbol from buied where userid=:userid group by symbol having shares >=1",userid=session["user_id"])
    nameofsymbol={}
    for stock in b:
        nameofsymbol[stock["symbol"]]=lookup(stock["symbol"])
    return render_template("portfolio.html",b=b,v=v,nameofsymbol=nameofsymbol)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        shares = int(request.form.get("shares"))

        if quote == None:
            return apology("invalid symbol", 400)
        if shares <= 0:
            return apology("invalid shares", 400)
        rows = db.execute("select * from users where id=:id",id=session["user_id"])
        cash = rows[0]["cash"]
        saham = quote["price"]
        total = shares * saham

        if total > cash:
            return apology("no engouh money", 400)
        db.execute("update  users set cash=cash-:totalprice where id=:id",totalprice=total,id=session["user_id"])
        dm=db.execute("select symbol from buied where userid = :userid and symbol = :symbol",userid=session["user_id"], symbol = request.form.get("symbol") )
        # checkifexitsymbol=dm[0]['symbol']
        db.execute("insert into history (userid,symbol,shares,price) values(:userid,:symbol,:shares,:price)",userid = session["user_id"],
         symbol = request.form.get("symbol"), shares =1*int(request.form.get("shares")), price = saham)
        if dm:
            db.execute("update  buied set shares = shares+ :sharesin",sharesin=shares)
        else:
            db.execute("insert into buied (userid,symbol,shares,priceofeachshare,date) values (:userid,:symbol,:shares,:price,datetime('now'))",
            userid=session["user_id"],symbol=request.form.get("symbol"),shares=shares,price=quote["price"])

        flash("Bought!")
        return redirect(url_for("index"))

    # User reached route via GET (as by clicking a link or via redi)
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    return jsonify("TODO")

@app.route("/addcash", methods=["GET", "POST"])
@login_required
def addcash():
    if request.method == "POST":

        if  request.form.get("addcash") or int(request.form.get("addcash")) < 0 :
            db.execute("update users set cash = cash + :addcas  where id = :id",
            addcas = int(request.form.get("addcash"))
            ,id = session["user_id"])
            return redirect(url_for("index"))
    else:
        return render_template("addcash.html")



@app.route("/history")
@login_required
def history():
    r=db.execute("select * from history where userid = :userid", userid = session["user_id"] )
    symdic= {}
    for i in r:
        symdic[i['symbol']]=lookup(i['symbol'])


    return render_template("history.html",r=r,symdic=symdic)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():


    """Get stock quote."""

    if request.method == "POST":
        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("invalid symbol", 400)

        return render_template("quoted.html", quote=quote)

    # User reached route via GET (as by clicking a link or via redi)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("not username")
        elif not request.form.get("password"):
            return apology("not password")
        elif not request.form.get("confirmation")==request.form.get("password"):
            return apology("password not match",400)
        hash = generate_password_hash(request.form.get("password"))
        user = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)",username=request.form.get("username"),hash=hash)

        if not user:
            return apology("invalid username")

        session["user_id"] = user

        # Display a flash message
        flash("Registered!")

        # Redirect user to home page
        return redirect(url_for("index"))
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    s=db.execute("select DISTINCT symbol from buied ")
    ss={}
    for n in s:
        ss[n["symbol"]]=lookup(n["symbol"])


    """Sell shares of stock"""
    # return apology("TODO"
    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("invalid symbol",400)
        if not request.form.get("shares"):
            return apology("invalid shares",400)
        symbolform = request.form.get("symbol")
        sharesform = int(request.form.get("shares"))
        quote = lookup(request.form.get("symbol"))


        dd = db.execute("select SUM(shares) as sharess from buied where  userid=:userid and symbol=:symbol",userid=session["user_id"],symbol=symbolform)
        v = dd[0]["sharess"]
        if dd[0]["sharess"] >= 1 and dd[0]["sharess"] >= sharesform:


            cashdb = db.execute("select cash from users where id=:id",id=session["user_id"])
            cash = cashdb[0]["cash"]
            sharetotal = dd[0]["sharess"]
            quote = lookup(request.form.get("symbol"))
            priceofeachshares=quote["price"]
            cashincrement = priceofeachshares * sharetotal
            cash = cash + cashincrement
            cashh=db.execute("update users set cash = :cash where id=:userid",cash = cash,userid = session["user_id"])
            db.execute("insert into history (userid,symbol,shares,price) values(:userid,:symbol,:shares,:price)",userid = session["user_id"],
         symbol = request.form.get("symbol"), shares =-1*int(request.form.get("shares")), price = priceofeachshares)
            if (v - sharesform) == 0:
                db.execute("delete from buied where userid=:userid",userid=session["user_id"])
            else:
                db.execute("update buied set shares  = :sha where userid=:userid and symbol = :symbol",sha=v - sharesform,userid=session["user_id"],symbol= symbolform)
                flash("sold!!!!!!!!!!!!")

            return redirect(url_for("index"))
            # return apology("invalid shares",487700)
    else:
        return render_template("sell.html",s=s,ss=ss)



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
