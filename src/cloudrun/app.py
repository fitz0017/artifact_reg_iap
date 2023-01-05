from flask import Flask, request, session 

app = Flask(__name__)

@app.route('/')
def index():
    page = """"""
    f = open('index.html')
    page = f.read()
    f.close()
    # page += f"Welcome, {}"
    return page

# Login processing will need to integrate IAP
@app.route('/login')
def login():
    pass

#Secondary page after login to allow creation of 60min token for auth with AR
@app.route('/request_token')
def request_token():
    pass


app.run(host="0.0.0.0", port=5000)