import os
import sqlite3

# import json to load JSON data to a python dictionary
import json

from flask import Flask, redirect, request, url_for, render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from oauthlib.oauth2 import WebApplicationClient
import requests

from db import init_db_command
from user import User

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)

try:
    init_db_command()
except sqlite3.OperationalError:
    pass  # Assume it's already been created

client = WebApplicationClient(GOOGLE_CLIENT_ID)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def index():
    if current_user.is_authenticated:
        return (
            '<a class="button" href="/logout">Logout</a>'
            '<p><a class="button" href="/about">About</a></p>'
            '<p><a class="button" href="/useragent">Useragent</a></p>'
            '<p><a class="button" href="/list/city">Weather</a></p>'
        )
    # return render_template("index.html")

    else:
        return '<a class="button" href="/login">Google Login</a>'


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@app.route("/list/city", methods=['POST', 'GET'])
def weather():
    '''website_url = requests.get('https://www.gismeteo.by/catalog/').text
    soup = BeautifulSoup(website_url, 'lxml')
    print(soup.prettify())
    country = input("Enter your country: ")'''
    # return ("<p>Your country is {}!</p>".format(requests.args.get('language')) )
    '''
    if request.method == 'POST':
        city = request.form['city']
    else:
        # for default name mathura
        city = 'minsk'

        # your API key will come here
    api = "82b2ee0b5f8eefc04b2a336c106bc800"

    # source contain json data from api
    source = urllib.request.urlopen(
        'https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=' + api).read()

    # converting JSON data to a dictionary
    list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' '
                      + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    print(data)
    return render_template('index.html', data=data)
'''

    import requests
    s_city = "Petersburg,RU"
    city_id = 0
    appid = "82b2ee0b5f8eefc04b2a336c106bc800"
    data = "Error ^("
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        print("conditions:", data['weather'][0]['description'])
        print("temp:", data['main']['temp'])
        print("temp_min:", data['main']['temp_min'])
        print("temp_max:", data['main']['temp_max'])
        return render_template('index.html', data=data)
    except Exception as e:
        print("Exception (find):", e)
        pass
    return render_template('index.html', data=data)


@app.route("/useragent")
def useragent():
    user_agent = request.user_agent
    return (
        '<p>Your platform is: {}</p>'
        '<p>Your browser is: {}</p>'.format(user_agent.platform, user_agent.browser)
    )


@app.route("/about")
def about():
    return (
        "<p>Hello, {}! You're logged in! Email: {}</p>"
        "<div><p>Google Profile Picture:</p>"
        '<img src="{}" alt="Google profile pic"></img></div>'.format(
            current_user.name, current_user.email, current_user.profile_pic,
        )
    )


@app.route("/login")
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)

    login_user(user)

    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(ssl_context="adhoc", debug=True)
