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
    age = False
    bmr_result = False
    name = False
    tdee = False
    result_tdee = False
    limit_cal = False
    if request.method == 'POST':
        name = request.form['name']
        weight = request.form['weight']
        height = request.form['height']
        age = request.form['age']
        gender = request.form['gender']
        tdee = request.form['tdee']
        #BMI Calulator
        bmi_result = float(weight)/(float(height)/100)**2
        bmi_result = round(bmi_result, 2)
        #BMR Calulator
        if gender == 'men':
            bmr_result = 66 + (13.7*float(weight)) + (5*float(height)) - (6.8*int(age))
            bmr_result = round(bmr_result, 1)
        if gender == 'famale':
            bmr_result = 665 + (9.6*float(weight)) + (1.8*float(height)) - (4.7*int(age))
            bmr_result = round(bmr_result, 1)
        #TDEE
        if tdee == 'nowo':
            result_tdee = bmr_result*1.2
        if tdee == 'wo1':
            result_tdee = bmr_result*1.375
        if tdee == 'wo2':
            result_tdee = bmr_result*1.55
        if tdee == 'wo3':
            result_tdee = bmr_result*1.725
        if tdee == 'wo4':
            result_tdee = bmr_result*1.9
        result_tdee = round(result_tdee, 1)

        #หากต้องการลดน้ำหนัก
        limit_cal = result_tdee - 500
        limit_cal = round(limit_cal, 1)
        
        


        #Session
        session['name'] = name
        session['bmi'] = bmi_result
        session['bmr'] = bmr_result
        session['tdee'] = result_tdee
        session['limit_cal'] = limit_cal
    return render_template("index.html")


@app.route('/dietplanning', methods=['GET','POST'])
def Diet_Planning():

    mission = False
    days = False
    if request.method == 'POST':
        mission = request.form['mission']
        days = request.form['days']

    return render_template("index.html")


# @app.route('/test',methods=['GET','POST'])
# def testsm():
#     name = False
#     age = False
#     cars = False
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         session['name']=name
#         cars = request.form['cars']
#     return render_template("test.html",name=name,age=age,cars=cars,bm=session['bmr'])

@app.route('/logout')
def logout():
    session['name'] = None
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)