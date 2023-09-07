from flask import Flask, flash, request, session, Response, url_for, send_from_directory, current_app, \
    send_file, render_template
import pymysql
app=Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY']='7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/registration")
def registration():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/update")
def update():
    return render_template('update.html')

@app.route("/delete")
def delete():
    return render_template('delete.html')

@app.route("/search")
def search():
    return render_template('search.html')

@app.route("/user_search")
def user_search1():
    return render_template('user_search')



@app.route("/user_register",methods=['GET','POST'])
def user_register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        contact=request.form['contact']
        address=request.form['address']
        city=request.form['city']
        pincode=request.form['pincode']

        conn=pymysql.connect(user='root',password='',host='localhost', database='bbb',charset='utf8')
        cursor=conn.cursor()
        cursor.execute("insert into blog_site values('"+name+"','"+email+"','"+password+"','"+contact+"','"+address+"','"+city+"','"+pincode+"')")
        conn.commit()
        cursor.close()
        return render_template('register.html')

@app.route("/user_login",methods=['GET','POST'])
def user_login():
    msg=None
    if request.method=='POST':
        n=request.form['email']
        g=request.form['password']
        n1=str(n)
        g1=str(g)
        q=("SELECT * from blog_site where email='"+str(n1)+ "' and password='" +str(g)+"'")
        conn = pymysql.connect(user='root', password='', host='localhost', database='bbb', charset='utf8')
        cursor = conn.cursor()
        cursor.execute(q)
        data=cursor.fetchall()
        check=len(data)
        if check==0:
            return render_template("login.html")
        else:
            return render_template(("login.html"))

@app.route("/user_update",methods=['GET','POST'])
def user_update():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        contact=request.form['contact']
        address=request.form['address']
        city=request.form['city']
        pincode=request.form['pincode']

        conn = pymysql.connect(user='root', password='', host='localhost', database='bbb', charset='utf8')
        cursor = conn.cursor()
        cursor.execute("update  blog_site set name='"+str(name)+"',email='"+str(email)+"',password='"+str(password)+"',contact='"+str(contact)+"',address='"+str(address)+"',city='"+str(city)+"',pincode='"+str(pincode)+"' where email='"+str(email)+"'")
        conn.commit()
        cursor.close()
        return render_template("update.html")

@app.route("/view")
def view():
    conn = pymysql.connect(user='root', password='', host='localhost', database='bbb', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT name,email,password,contact,address,city,pincode FROM blog_site")
    data=cursor.fetchall()
    # cursor.close()
    print(data)
    return render_template('view.html',items=data)

@app.route("/user_delete",methods=['GET','POST'])
def user_delete():
    if request.method=='POST':
        email=request.form['email']

        conn1 = pymysql.connect(user='root', password='', host='localhost', database='bbb', charset='utf8')
        cursor1 = conn1.cursor()
        cursor1.execute("DELETE  from blog_site  where email='" + str(email) + "'")
        conn1.commit()
        cursor1.close()
        return render_template("delete.html")
    # return render_template("delete.html")

@app.route("/user_search",methods=['GET','POST'])
def user_search():
    if request.method=='POST':
        email=request.form['search']
        conn = pymysql.connect(user='root', password='', host='localhost', database='bbb', charset='utf8')
        cursor = conn.cursor()
        cursor.execute("SELECT name,email,password,contact,address,city,pincode FROM blog_site where email='"+str(email)+"'")
        data = cursor.fetchall()
        # cursor.close()
        print(data)
        return render_template('user_search.html', items=data)
    return render_template('search.html')

        # conn1 = pymysql.connect(user='root', password='', host='localhost', database='bbb', charset='utf8')




if __name__=='__main__':
    app.run(debug=True,use_reloader=True,host="0.0.0.0")