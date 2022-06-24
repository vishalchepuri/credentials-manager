import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import secure


cred = credentials.Certificate("D:/python/credentials-manager/myfile.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def check_encryption_password(email, password):
    doc = db.collection(email).document('Credential Manager').get()
    data = doc.to_dict()
    if secure.decrypt(data['Password'], password):
        return True
    return False


def get_result(user_id):
    users_ref = db.collection(user_id)
    res = {}
    for doc in users_ref.get():
        res[doc.id] = doc.to_dict()
    return res


def get_document(user_id, document):
    users_ref = db.collection(user_id).document(document)
    doc = users_ref.get()
    res = doc.to_dict()
    return res


def update_document(email, website, data, password):
    if check_encryption_password(email, password):
        city_ref = db.collection(email).document(website)
        city_ref.update(data)
    else:
        pass


def set_result(email, website, data, password):
    if check_encryption_password(email, password):
        db.collection(email).document(website).set(data)
    else:
        pass


def add_test_data(email, encryption_password):
    website = 'Credential Manager'
    data = {
        'Username': secure.encrypt('test@gmail.com', encryption_password),
        'Password': secure.encrypt('ABCD@123', encryption_password),
        'Backupcodes': secure.encrypt('123456,754321,12323,746645,234242', encryption_password)
    }
    db.collection(email).document(website).set(data)


def delete_document(email, website, password):
    if check_encryption_password(email, password):
        db.collection(email).document(website).delete()
    else:
        pass


def codes(code):
    access_codes = db.collection('Access codes').get()
    lst = []
    for doc in access_codes:
        lst.append(doc.id)
    if code in lst:
        db.collection('Access codes').document(code).delete()
        return True
    return False
