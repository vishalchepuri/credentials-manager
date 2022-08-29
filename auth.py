import pyrebase
config = {
        "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": "",
    "databaseURL": ""
    }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def email_verification(token):
    try:
        auth.send_email_verification(token)
    except:
        pass

def signup(email="test", password="test"):
    try:
        create = auth.create_user_with_email_and_password(email, password)
        email_verification(create['idToken'])
        return create
    except Exception as e:
        return None


def login(email="test", password="test"):
    try:
        return auth.sign_in_with_email_and_password(email, password)
    except:
        return None


def forgot_password(email):
    try:
        auth.send_password_reset_email(email)
    except:
        pass




