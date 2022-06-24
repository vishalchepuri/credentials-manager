import time
from flask import Flask, render_template, request, flash
import auth
import firestore
import secure
check, flag, email, encryption_password = False, 0, "", ""
app = Flask(__name__)
app.secret_key = "AES"



def password_strength(paswd):
    c, s, n = 0, 0, 0
    for i in paswd:
        if i.isdigit():
            n = 1
        elif i.isalpha():
            c = 1
        elif not (i.isdigit() and i.isalpha()):
            s = 1
    if len(paswd) > 8 and c + s + n == 3:
        return True
    return False


@app.route('/')
def signin():
    global check, flag, email, encryption_password
    check, flag, email, encryption_password = False, 0, "", ""
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/resetpassword')
def resetpassword():
    return render_template('forgotpassword.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    global check
    global email, flag
    if request.method == 'POST':
        email = str(request.form['username'])
        password = str(request.form['password'])
        check = auth.signup(email, password)
        flag = 1
        if check:
            return render_template('encryption_password.html')
        else:
            # ^ (?=.*[A-Za-z])(?=.* \d)(?=.*[@ $! % *  # ?&])[A-Za-z\d@$!%*#?&]{8,}$
            if len(password) <= 5:
                flash(u'Invalid password provided')
            return render_template('login.html', dict=dict)


@app.route('/login', methods=['POST', 'GET', 'PATCH'])
def login():
    global check
    global email
    if request.method == 'POST':
        email = str(request.form['username'])
        password = str(request.form['password'])
        check = auth.login(email, password)
        if check:
            try:
                flash('dafdfsdfds')
            except Exception as e:
                print(e.args)
            return render_template('encryption_password.html')
        else:
            return render_template('signup.html')


@app.route('/test', methods=['POST', 'GET'])
def test():
    return render_template('add_data.html')


@app.route('/table', methods=['POST', 'GET'])
def table():
    global check
    data = firestore.get_result(email)
    decryptedData = {}
    for i in data:
        decryptedData[i] = {}
        decryptedData[i]["Username"] = secure.decrypt(data[i]['Username'], encryption_password)
        decryptedData[i]["Password"] = secure.decrypt(data[i]['Password'], encryption_password)
        decryptedData[i]["Backupcodes"] = secure.decrypt(data[i]['Backupcodes'], encryption_password)
    return render_template('table.html', data=decryptedData)


@app.route('/edit/<id>', methods=['GET'])
def edit(user_id):
    global check
    decryptedData = {}
    if user_id == 'Website' or user_id == 'Credential Manager':
        return table()
    data = firestore.get_document(email, ID)
    decryptedData["Type"] = ID
    decryptedData["Username"] = secure.decrypt(data['Username'], encryption_password)
    decryptedData["Password"] = secure.decrypt(data['Password'], encryption_password)
    decryptedData["Backupcodes"] = secure.decrypt(data['Backupcodes'], encryption_password)
    # print(decryptedData)
    return render_template("edit.html", data=decryptedData)


@app.route('/update_data', methods=['POST', 'GET'])
def update_data():
    global check
    global encryption_password
    decryptedData = {}
    website = str(request.form['type'])
    decryptedData['Username'] = secure.encrypt(str(request.form['username']), encryption_password)
    decryptedData['Password'] = secure.encrypt(str(request.form['password']), encryption_password)
    decryptedData['Backupcodes'] = secure.encrypt(str(request.form['backupcodes']), encryption_password)
    # print(decryptedData)
    firestore.update_document(email, website, decryptedData, encryption_password)
    data = firestore.get_result(email)
    # print(type(data))
    decryptedData = {}
    for i in data:
        decryptedData[i] = {}
        decryptedData[i]["Username"] = secure.decrypt(data[i]['Username'], encryption_password)
        decryptedData[i]["Password"] = secure.decrypt(data[i]['Password'], encryption_password)
        decryptedData[i]["Backupcodes"] = secure.decrypt(data[i]['Backupcodes'], encryption_password)

    return render_template('table.html', data=decryptedData)


@app.route('/add_data', methods=['POST', 'GET', 'PATCH'])
def add_data():
    global check
    website = str(request.form['website'])
    user_id = email
    data = {
        u'Username': secure.encrypt(str(request.form['username']), encryption_password),
        u'Password': secure.encrypt(str(request.form['password']), encryption_password),
        u'Backupcodes': secure.encrypt(str(request.form['backupcodes']), encryption_password)
    }
    firestore.set_result(user_id, website, data, encryption_password)
    return render_template('add_data.html')


@app.route('/done', methods=['POST', 'GET'])
def encryption_password():
    global encryption_password
    if request.method == 'POST':
        encryption_password = str(request.form['encryption_password'])
        if flag:
            firestore.add_test_data(email, encryption_password)
            time.sleep(1)
        decryptedData = {}
        data = firestore.get_result(email)
        for i in data:
            decryptedData[i] = {}
            decryptedData[i]["Username"] = secure.decrypt(data[i]['Username'], encryption_password)
            decryptedData[i]["Password"] = secure.decrypt(data[i]['Password'], encryption_password)
            decryptedData[i]["Backupcodes"] = secure.decrypt(data[i]['Backupcodes'], encryption_password)
        return render_template('table.html', data=decryptedData)
    return render_template('login.html')


@app.route('/forgotpassword', methods=['POST', 'GET'])
def forgotpassword(email="test"):
    auth.forgot_password(email)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
