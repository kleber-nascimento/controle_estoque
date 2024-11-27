from flask import Flask, render_template, redirect, request, flash
import json
import ast

app = Flask(__name__)
app.config['SECRET_KEY'] = 'INREDES'

logon = False

@app.route("/")
def home():
    global logon
    logon = False
    return render_template("login.html")

@app.route("/adm")
def adm():
    if logon == True:
            with open('users.json') as userTemp:
                users = json.load(userTemp)
            return render_template("admin.html",user=users)

    if logon == False:
        return redirect('/')
    
    

@app.route("/login", methods=['POST'])
def login():

    global logon

    email = request.form.get('email')
    password = request.form.get('password')

    with open('users.json') as userTemp:
        users = json.load(userTemp)
        cont = 0
        for user in users:
            cont += 1

            if email == "admin@admin" and password == "admin":
                logon = True
                return redirect('/adm')

            if user['email'] == email and user['password'] == password:
                return render_template('user.html')
            
            if cont >= len(users):
                flash('Usuário inválido')
                return redirect('/')


@app.route('/addUser', methods=['POST'])
def addUser():
    global logon 
    user = []
    email = request.form.get('email')
    password = request.form.get('password')
    user = [
        {
            "email": email,
            "password": password
        }
    ]
    with open('users.json') as userTemp:
        users = json.load(userTemp)

    newUser = user + users

    with open('users.json', 'w') as recordTemp:
        json.dump(newUser, recordTemp, indent=4)
    logon = True
    flash(f'{email} Cadastrado com Sucesso!')
    return redirect('/adm')


@app.route('/delUser', methods=['POST'])
def delUser():
    global logon
    logon = True
    user = request.form.get('delUser')
    userDict = ast.literal_eval(user)
    name = userDict['email']
    with open('users.json') as tempUsers:
        userJson = json.load(tempUsers)
        for c in userJson:
            if c == userDict:
                userJson.remove(userDict)
                with open('users.json', 'w') as willbeDelUser:
                    json.dump(userJson, willbeDelUser, indent=4)

   
    print(type(userDict))
    flash(F'Excluido')
    return redirect('/adm')



if __name__ in "__main__":
    app.run(debug=True)