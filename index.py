from flask import Flask,render_template,request,session,redirect
import function as fn
import data

#เรียกการทำงาน Flask
app = Flask(__name__)
#ตั้งค่า Secret Key เพื่อให้ส่งค่าแบบ POST ได้
app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():

    #test
    session['mylist'] = list()
    #endtest
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
    weight = False
    height = False
    gender = False
    bmi_result = False
    age = False
    bmr_result = False
    name = False
    tdee = False
    result_tdee = False
    limit_cal = False
    bmi_status = False
    test_data = False
    if request.method == 'POST':
        name = request.form['name']
        weight = request.form['weight']
        height = request.form['height']
        age = request.form['age']
        gender = request.form['gender']
        tdee = request.form['tdee']
    #BMI Calulator
    bmi_result = fn.bmi(weight, height)
    #BMI Status
    bmi_status = fn.bmi_status(bmi_result)
    bmi_status = data.BMI[bmi_status]
    #BMR Calulator
    bmr_result = fn.bmr(weight, height, age, gender)
    #TDEE
    result_tdee = fn.tdee(tdee, bmr_result)

    #หากต้องการลดน้ำหนัก
    limit_cal = result_tdee - 500
    limit_cal = round(limit_cal, 1)
    


    #Session
    session['name'] = name
    session['bmi'] = bmi_result
    session['bmr'] = bmr_result
    session['tdee'] = result_tdee
    session['limit_cal'] = limit_cal
    session['bmi_status'] = bmi_status
    return render_template("result.html")

chc = False


@app.route('/test',methods=['GET','POST'])
def testsm():
    name = False
    age = False
    cars = False

    # lister = request.args.get("sum")
    if request.method == 'POST':
        
        ig = int(request.form['sum'])
        # name = request.form['name']
        # age = request.form['age']
        session['name']=name
        # cars = request.form['cars']
        # lister.append(request.form['sum'])
        session['mylist'].append(int(request.form['sum']))

    # return render_template("test.html",name=name,age=age,cars=cars,bm=session['bmr'],st='good')
    return render_template("test.html")

@app.route('/logout')
def logout():
    session['name'] = None
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)