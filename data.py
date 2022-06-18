import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("D:/python/credentials-manager/myfile.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# ID = "Manichandra"
# backup_codes = "213213,21321312,23,213,123,213,213,21312,3,2,13,12,3,213,2,13,21,3"
# password = "Vishal@123"
# enc_key = "1234"
# username = 'Mani'
# type = 'Facebook'
# user_ref = db.collection(ID).document(type)
# user_ref.set({
#     'Username': username,
#     'Password': u'dsafd',
#     'Backupcodes': u'cryptocode.encrypt(backup_codes, enc_key)',
# })
# print("done")

# temp = db.collection('Vishalchepuri1').document('Instagram').get()
# print(temp.to_dict())

users_ref = db.collection(u'Vishalchepuri1')
docs = users_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
