from flask import Flask, request, session
import google.auth
import subprocess
# TODO - understand google auth library for python to print bearer token impresonating
# the artifact registry account already created.

app = Flask(__name__)


@app.route('/')
def index():
    page = """"""
    f = open('index.html')
    page = f.read()
    f.close()
    # page += f"Welcome, {}"
    # creds = google.auth.default()
    # print(repr(creds))
    creds = subprocess.check_output(
        "gcloud auth print-access-token", shell=True)
    print(creds.strip())
    page = page.replace("{{ creds }}", repr(creds))
    return page

# Login processing will need to integrate IAP


@ app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]
        if username == "kevin" and password == "password123":
            return "<h1>get token</h1>"

        # Secondary page after login to allow creation of 60min token for auth with AR


@ app.route('/request_token')
def request_token():
    pass


app.run(host="0.0.0.0", port=5000)
