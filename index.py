from flask import Flask,render_template,request,session,redirect
import function as fn
import data

#เรียกการทำงาน Flask
app = Flask(__name__)
#ตั้งค่า Secret Key เพื่อให้ส่งค่าแบบ POST ได้
app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():

    #session
    session['forlist'] = False
    session['sumcal'] = 0
    session['foods'] = list()
    session['foodscal'] = list()
    #test
    session['mylist'] = []
    
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

@app.route('/foods',methods=['GET','POST'])
def foodscal():
    name=False
    food = False
    foodcal = False
    sumcal = False
    countfoods = False
    foods=data.foods
    if request.method == 'POST':
        session['forlist'] = name
        if request.form['submit'] == 'ส่งข้อมูล':
            food = request.form['food']

            session['foods'].append(foods[food]['name'])
            session['foodscal'].append(foods[food]['cal'])
        if request.form['submit'] == 'ส่งข้อมูลกำหนดเอง':
            food = request.form['food']
            foodcal = int(request.form['foodcal'])

            session['foods'].append(food)
            session['foodscal'].append(foodcal)

    countfoods = len(session['foods'])

    for i in session['foodscal']:
        sumcal = sumcal+i
    

    return render_template("foods.html",menu=foods,c=countfoods,s=sumcal)


@app.route('/test',methods=['GET','POST'])
def testsm():
    mmmm = []
    name = False
    age = False
    cars = False

    testinput = False

    # lister = request.args.get("sum")
    if request.method == 'POST':
        session['forlist'] = name
        
        # name = request.form['name']
        # age = request.form['age']
        if request.form['submit'] == 'ส':
            testinput = request.form['testinput']
        # cars = request.form['cars']
        # lister.append(request.form['sum'])
        if request.form['submit'] == 'สส':

            session['mylist'].append(request.form['sum'])

    # return render_template("test.html",name=name,age=age,cars=cars,bm=session['bmr'],st='good')
    return render_template("test.html",ttt=testinput)

@app.route('/logout')
def logout():
    session['name'] = None
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)