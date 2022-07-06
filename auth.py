import pyrebase
config = {
        "apiKey": "AIzaSyDEHCenBLxNRtsS8CBbWYqkqjl94bnVzyY",
    "authDomain": "credential-manager-a0d90.firebaseapp.com",
    "projectId": "credential-manager-a0d90",
    "storageBucket": "credential-manager-a0d90.appspot.com",
    "messagingSenderId": "816081903625",
    "appId": "1:816081903625:web:5ebaae9420b132649d18d8",
    "measurementId": "G-MYKFJQMJHY",
    "databaseURL": "https://credential-manager-a0d90.firebaseio.com"
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




