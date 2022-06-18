from flask import Flask, redirect, url_for, render_template, request
import auth
import firestore

import secure

app = Flask(__name__)
p = 'password123'


# def table():
#     data = firestore.get_result('Vishalchepuri1')
#     decryptedData = {}
#     for i in data:
#         decryptedData[i] = {}
#         decryptedData[i]["Username"] = secure.decrypt(data[i]['Username'], 'password123')
#         decryptedData[i]["Password"] = secure.decrypt(data[i]['Password'], 'password123')
#         decryptedData[i]["Backupcodes"] = secure.decrypt(data[i]['Backupcodes'], 'password123')
#     return render_template('table.html', data=decryptedData)


@app.route('/')
def signin():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    # dic = {'dafd':'adfads'}
    # # if request.method == 'POST':
    # #     email = str(request.form['username'])
    # #     password = str(request.form['paswd'])
    # #     if auth.signup(email, password):
    # #         dict['msg'] = "Another account is using the same email."
    # #     else:
    # #         dict['msg'] = "Done"
    data = firestore.get_result('Vishalchepuri1')
    # print(type(data))
    decryptedData = {}
    for i in data:
        decryptedData[i] = {}
        decryptedData[i]["Username"] = secure.decrypt(data[i]['Username'],'password123')
        decryptedData[i]["Password"] = secure.decrypt(data[i]['Password'],'password123')
        decryptedData[i]["Backupcodes"] = secure.decrypt(data[i]['Backupcodes'],'password123')

    return render_template('table.html', data=decryptedData)
    # return render_template('result.html', dict=dic)





@app.route('/edit/<id>', methods=['GET'])
def edit(id):
    # print("got it")
    data = firestore.get_document("Vishalchepuri1", id)
    decryptedData = {}
    decryptedData["Type"]=id
    decryptedData["Username"] = secure.decrypt(data['Username'], 'password123')
    decryptedData["Password"] = secure.decrypt(data['Password'], 'password123')
    decryptedData["Backupcodes"] = secure.decrypt(data['Backupcodes'], 'password123')
    # print(decryptedData)
    return render_template("edit.html", data=decryptedData)


@app.route('/update_data', methods=['POST', 'GET'])
def update_data():
    decryptedData={}
    website = str(request.form['type'])
    decryptedData['Username'] = secure.encrypt(str(request.form['username']),p)
    decryptedData['Password'] = secure.encrypt(str(request.form['password']),p)
    decryptedData['Backupcodes'] = secure.encrypt(str(request.form['backupcodes']),p)
    print(decryptedData)
    firestore.update_document(website, decryptedData)
    data = firestore.get_result('Vishalchepuri1')
    # print(type(data))
    decryptedData = {}
    for i in data:
        decryptedData[i] = {}
        decryptedData[i]["Username"] = secure.decrypt(data[i]['Username'], 'password123')
        decryptedData[i]["Password"] = secure.decrypt(data[i]['Password'], 'password123')
        decryptedData[i]["Backupcodes"] = secure.decrypt(data[i]['Backupcodes'], 'password123')

    return render_template('table.html', data=decryptedData)



@app.route('/login', methods=['POST', 'GET', 'PATCH'])
def login():
    dict = {}
    if request.method == 'POST':
        email = str(request.form['username'])
        password = str(request.form['paswd'])
        if auth.login(email, password):
            dict['msg'] = "Done"
        else:
            dict['msg'] = "The Email or password provided is incorrect.."
    return render_template('result.html', dict=dict)



if __name__ == '__main__':
    app.run(debug=True,port=5000)
