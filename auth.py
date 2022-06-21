import pyrebase
config = {
        "apiKey": "AIzaSyDLKJlcPE55UnP6iN1ziuiYEoRVEUPToTA",
        "authDomain": "learning-54b3e.firebaseapp.com",
        "databaseURL": "https://learning-54b3e-default-rtdb.firebaseio.com",
        "projectId": "learning-54b3e",
        "storageBucket": "learning-54b3e.appspot.com",
        "messagingSenderId": "290059634862",
        "appId": "1:290059634862:web:c56a7c7c8c5f1367ec053f",
        "measurementId": "G-23D5VEQXSH"
    }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def signup(email="test", password="test"):
    try:
        return auth.create_user_with_email_and_password(email, password)
    except Exception as e:
        return None



def login(email="test", password="test"):
    try:
        return auth.sign_in_with_email_and_password(email, password)
    except:
        return None

def forgot_password(email="test"):
    auth.send_password_reset_email()

