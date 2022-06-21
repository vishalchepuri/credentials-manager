from flask import Flask, render_template, request
import auth
import firestore
import secure
email = ""
encryption_password = ""
app = Flask(__name__)
check = False




@app.route('/')
def signin():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    global check
    global email
    if request.method == 'POST':
        email = str(request.form['username'])
        password = str(request.form['password'])
        check = auth.signup(email, password)
        if check:
            return render_template('encryption_password.html')
        else:
            return render_template('login.html', dict=dict)
    # data = firestore.get_result('Vishalchepuri1')
    # print(type(data))
    # decryptedData = {}
    # for i in data:
    #     decryptedData[i] = {}
    #     decryptedData[i]["Username"] = secure.decrypt(data[i]['Username'],'password123')
    #     decryptedData[i]["Password"] = secure.decrypt(data[i]['Password'],'password123')
    #     decryptedData[i]["Backupcodes"] = secure.decrypt(data[i]['Backupcodes'],'password123')
    #
    return render_template('add_data.html')
    # return render_template('result.html', dict=dic)

@app.route('/login', methods=['POST', 'GET', 'PATCH'])
def login():
    global check
    global email
    if request.method == 'POST':
        email = str(request.form['username'])
        password = str(request.form['password'])
        check = auth.login(email, password)
        if check:
            return render_template('encryption_password.html')
        else:
            return render_template('signup.html')


@app.route('/data', methods=['POST', 'GET'])
def table():
    global check
    data = firestore.get_result(email)
    decryptedData = {}
    for i in data:
        decryptedData[i] = {}
        decryptedData[i]["Username"] = secure.decrypt(data[i]['Username'], 'password123')
        decryptedData[i]["Password"] = secure.decrypt(data[i]['Password'], 'password123')
        decryptedData[i]["Backupcodes"] = secure.decrypt(data[i]['Backupcodes'], 'password123')
    return render_template('table.html', data=decryptedData)


@app.route('/edit/<id>', methods=['GET'])
def edit(id):
    global check
    # print("got it")
    if id == 'Website':
        pass
    data = firestore.get_document(email, id)
    decryptedData = {}
    decryptedData["Type"] = id
    decryptedData["Username"] = secure.decrypt(data['Username'], encryption_password)
    decryptedData["Password"] = secure.decrypt(data['Password'], encryption_password)
    decryptedData["Backupcodes"] = secure.decrypt(data['Backupcodes'], encryption_password)
    # print(decryptedData)
    return render_template("edit.html", data=decryptedData)


@app.route('/update_data', methods=['POST', 'GET'])
def update_data():
    global check
    global encryption_password
    decryptedData={}
    website = str(request.form['type'])
    decryptedData['Username'] = secure.encrypt(str(request.form['username']), encryption_password)
    decryptedData['Password'] = secure.encrypt(str(request.form['password']), encryption_password)
    decryptedData['Backupcodes'] = secure.encrypt(str(request.form['backupcodes']),encryption_password)
    # print(decryptedData)
    firestore.update_document(email,website, decryptedData,encryption_password)
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
    # if check:
    website = str(request.form['website'])
    id = email
    data = {
        u'Username': secure.encrypt(str(request.form['username']), encryption_password),
        u'Password': secure.encrypt(str(request.form['password']), encryption_password),
        u'Backupcodes': secure.encrypt(str(request.form['backupcodes']), encryption_password)
    }
    firestore.set_result(id, website, data)
    return render_template('add_data.html')

@app.route('/done', methods=['POST', 'GET'])
def encryption_password():
    global encryption_password
    if request.method == 'POST':
        # encryption_password = str(request.form['encryption_password'])
        # data = firestore.get_result(email)
        # decryptedData = {}
        # for i in data:
        #     decryptedData[i] = {}
        #     decryptedData[i]["Username"] = secure.decrypt(data[i]['Username'], encryption_password)
        #     decryptedData[i]["Password"] = secure.decrypt(data[i]['Password'], encryption_password)
        #     decryptedData[i]["Backupcodes"] = secure.decrypt(data[i]['Backupcodes'], encryption_password)
        return table()
    return render_template('login.html')


@app.route('/forgotpassword', methods=['POST', 'GET'])
def forgotpassword(email="test"):
    auth.forgot_password(email)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
