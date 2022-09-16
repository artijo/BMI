from flask import Flask,render_template,request,session,redirect

#เรียกการทำงาน Flask
app = Flask(__name__)
#ตั้งค่า Secret Key เพื่อให้ส่งค่าแบบ POST ได้
app.config['SECRET_KEY'] = 'mykey'



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test',methods=['GET','POST'])
def testsm():
    name = False
    age = False
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        session['name']=name
    return render_template("test.html",name=name,age=age)

@app.route('/logout')
def logout():
    session['name'] = None
    return redirect('/')

if __name__ == "__main__":
    app.run()