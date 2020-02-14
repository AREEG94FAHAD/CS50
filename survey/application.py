import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():

    # print(request.form.get("name"), request.form.get("language"))

    # if no values, return error.
    # if not request.form.get("email") or not request.form.get("password") or not request.form.get("address") or not request.form.get("address2") or not request.form.get("city") or not request.form.get("select") or not request.form.get("zip") or not request.form.get("check"):
    #     message = "You need to full all form"
    #     return render_template("error.html", message=message)

    with open("./survey.csv", "a") as f:
        csv_f = csv.writer(f, delimiter=",")
        csv_f.writerow([request.form.get('email'),
                        request.form.get('password'),
                        request.form.get('address'),
                        request.form.get('address2'),
                        request.form.get('city'),
                        request.form.get('select'),
                        request.form.get('zip'),
                        request.form.get('check')])

    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():

    forms = []

    with open("./survey.csv", "r") as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            forms.append(row)

    return render_template("sheet.html", forms=forms)
    # return render_template("error.html", message="TODO")