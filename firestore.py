import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import json
import secure
from flask import Flask

cred = credentials.Certificate("D:/python/credentials-manager/myfile.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def get_result(ID,paswd='password123'):
    users_ref = db.collection(ID)
    res = {}
    for doc in users_ref.get():
        res[doc.id] = doc.to_dict()
    # print(res)
    return res


def get_document(ID, document ,paswd='password123'):
    users_ref = db.collection(ID).document(document)
    doc = users_ref.get()
    res = doc.to_dict()
    print(res)
    return res


# get_result('Vishalchepuri1')

# def set_result(ID,Type,data):
#     res = db.collection(ID).document(Type).set(data)
#
# def set_re(ID=0, backup_codes=0, password=0, enc_key=0, username=0):
#     ID = "123456"
#     backup_codes = "213213,21321312,23,213,123,213,213,21312,3,2,13,12,3,213,2,13,21,3"
#     password = "Vishal@123"
#     enc_key = "1234"
#     username = 'Mani'
#     type = 'Facebook'
#     user_ref = db.collection(ID).document(type)
#     user_ref.set({
#         'Username': username,
#         'Password': secure.encrypt(password, enc_key),
#         'Backupcodes': secure.encrypt(backup_codes, enc_key),
#     })
#
#
# ID = "Manichandra"
# backup_codes = "213213,21321312,23,213,123,213,213,21312,3,2,13,12,3,213,2,13,21,3"
# password = "Vishal@123"
# enc_key = "1234"
# username = 'Mani'
# type = 'Facebook'
# user_ref = db.collection(ID).document(type)
# user_ref.set({
#     'Username' : username,
#     'Password': 'dsafd',
#     'Backupcodes': 'cryptocode.encrypt(backup_codes, enc_key)',
# })
# print("done")
#
# import pyrebase
#
# config = {
#         "apiKey": "AIzaSyDLKJlcPE55UnP6iN1ziuiYEoRVEUPToTA",
#         "authDomain": "learning-54b3e.firebaseapp.com",
#         "databaseURL": "https://learning-54b3e-default-rtdb.firebaseio.com",
#         "projectId": "learning-54b3e",
#         "storageBucket": "learning-54b3e.appspot.com",
#         "messagingSenderId": "290059634862",
#         "appId": "1:290059634862:web:c56a7c7c8c5f1367ec053f",
#         "measurementId": "G-23D5VEQXSH"
#     }
# firebase = pyrebase.initialize_app(config)
# db = firebase.cl()
