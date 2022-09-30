import pyrebase
from getpass import getpass


firebaseConfig = {
  "apiKey": "",
  "authDomain": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "measurementId": "",
  'databaseURL': '',
}


firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()

a = auth.create_user_with_email_and_password('vifadfd@faa.cod','dsafds@123')
print(a)
