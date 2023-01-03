from flask import Flask, render_template,url_for,session,request,flash,redirect

app = Flask(__name__,template_folder="templates",
            static_folder="static")


@app.route('/')
def home():
    return render_template('index.html')

#
#
#
#
#
#
#

@app.route('/Login')
def Login():
    return render_template("login.html")
#
# @app.route("/Login",methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         session.pop('username', None)
#         log = request.form
#         username = log['username']
#         password = log['password']
#
#         conn = py.connect(database_connect)
#         cursor = conn.cursor()
#
#         insertion_statement = "SELECT *  FROM dbo.record WHERE username = '" + username + "' and password='" +password+"'"
#         cursor.execute(insertion_statement)
#         rows = cursor.execute(insertion_statement)
#         rows = rows.fetchall()
#         if len(rows) == 1:
#             session['username'] = log['username']
#             session["log"] = True
#             return render_template('home.html', name=session['username'])
#         else:
#             flash("Please enter correct name and password", "danger")
#             return render_template("login.html")
#
#
#
@app.route('/Register')
def Register():
    return render_template("register.html")
#
# @app.route("/Register",methods=['GET','POST'])
# def register():
#     if request.method == "POST" :
#         signup = request.form
#         name = signup['name']
#         email_id = signup['email_id']
#         username = signup['username']
#         phone_number = signup['phone_number']
#         password = signup['password']
#         confirm_password = signup['confirm_password']
#
#         conn = py.connect(database_connect)
#         cursor = conn.cursor()
#
#         insertion_statement = "INSERT INTO dbo.record VALUES(?,?,?,?,?,?) "
#
#         data = [name,email_id,username,phone_number, password, confirm_password]
#         cursor.execute(insertion_statement, data)
#
#         if password == confirm_password :
#             cursor.commit()
#             cursor.close()
#             flash("You are registered and can login","success")
#             return render_template('login.html')
#         else :
#             flash("password does not match","danger")
#             return render_template("register.html")
#
#
@app.route("/blog")
def blog():
    return render_template("blog.html")



#
if __name__ == "__main__" :
    app.run(debug=True)