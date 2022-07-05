import pyrebase
from getpass import getpass


firebaseConfig = {
  "apiKey": "AIzaSyB9Kmo6Adz2lESIYWcUewS900CTq9HoMEg",
  "authDomain": "temp-f5544.firebaseapp.com",
  "projectId": "temp-f5544",
  "storageBucket": "temp-f5544.appspot.com",
  "messagingSenderId": "69666549650",
  "appId": "1:69666549650:web:a139672b8104e10c499b4b",
  "measurementId": "G-HKTQ9YG9PF",
  'databaseURL': 'https://temp-f5544.firebaseio.com',
}


firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()


# email = input("Please Enter Your Email Address : \n")
# password = getpass("Please Enter Your Password : \n")
#
# #create users
# user = auth.create_user_with_email_and_password(email, password)
# print("Success .... ")
#
#
#
# # login = auth.sign_in_with_email_and_password(email, password)
#
# #send email verification
# auth.send_email_verification(login['idToken'])
#
#
# #reset the password
# auth.send_password_reset_email(email)
#
# print("Success ... ")

a = auth.create_user_with_email_and_password('vifadfd@faa.cod','dsafds@123')
print(a)