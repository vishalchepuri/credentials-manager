import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import secure

cred = credentials.Certificate("D:/python/credentials-manager/myfile.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def check_encryption_password(email, website, password):
    doc = db.collection(email).document(website).get()
    data = doc.to_dict()
    if secure.decrypt(data['Password'], password)!='False':
        return True
    return False

def get_result(ID):
    users_ref = db.collection(ID)
    res = {}
    for doc in users_ref.get():
        res[doc.id] = doc.to_dict()
    return res

def get_document(ID, document):
    users_ref = db.collection(ID).document(document)
    doc = users_ref.get()
    res = doc.to_dict()
    return res


def update_document(email, website, data, password):
    if check_encryption_password(email, website, password):
        city_ref = db.collection(email).document(website)
        city_ref.update(data)
    else:
        pass

def set_result(email, website, data, password):
    if check_encryption_password(email, website, password):
        db.collection(email).document(website).set(data)


