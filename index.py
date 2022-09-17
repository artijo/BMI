from distutils.log import debug
from flask import Flask,render_template,request,session,redirect

#เรียกการทำงาน Flask
app = Flask(__name__)
#ตั้งค่า Secret Key เพื่อให้ส่งค่าแบบ POST ได้
app.config['SECRET_KEY'] = 'mykey'



@app.route('/', methods=['GET','POST'])
def index():
    weight = False
    height = False
    gender = False
    bmi_result = False
    if request.method == 'POST':
        weight = request.form['weight']
        height = request.form['height']
        gender = request.form['gender']
        bmi_result = float(weight)/(float(height)/100)**2
        bmi_result = round(bmi_result, 2)
    return render_template("index.html",w=weight,h=height,g=gender,r=bmi_result)

@app.route('/test',methods=['GET','POST'])
def testsm():
    name = False
    age = False
    cars = False
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        session['name']=name
        cars = request.form['cars']
    return render_template("test.html",name=name,age=age,cars=cars)

@app.route('/logout')
def logout():
    session['name'] = None
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)