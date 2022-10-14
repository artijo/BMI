from flask import Flask,render_template,request,session,redirect
import function as fn
import data

#เรียกการทำงาน Flask
app = Flask(__name__)
#ตั้งค่า Secret Key เพื่อให้ส่งค่าแบบ POST ได้
app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def result():
    weight = height = gender = bmi_result = age = bmr_result = name = tdee = result_tdee = limit_cal = bmi_status = bmi_tdee_des = False
    try:
        if request.method == 'POST':
            name = request.form['name']
            weight = request.form['weight']
            height = request.form['height']
            age = request.form['age']
            gender = request.form['gender']
            tdee = request.form['tdee']

    except:
        return redirect('/')

    else:
        try:
            #BMI Calulator
            bmi_result = fn.bmi(weight, height)
            #BMI Status
            bmi_status = fn.bmi_status(bmi_result)
            bmi_status = data.BMI[bmi_status]
            #BMR Calulator
            bmr_result = fn.bmr(weight, height, age, gender)
            #TDEE
            result_tdee = fn.tdee(tdee, bmr_result)
            bmi_tdee_des = fn.bmr_des(fn.bmi_status(bmi_result),result_tdee)

            #หากต้องการลดน้ำหนัก
            limit_cal = result_tdee - 500
            limit_cal = round(limit_cal, 1)
        except ZeroDivisionError:
            return redirect('/')

        else:
            #Session
            session['name'] = name
            session['bmi'] = bmi_result
            session['bmr'] = bmr_result
            session['tdee'] = result_tdee
            session['tdee_food'] = fn.tdee_food(fn.bmi_status(bmi_result),result_tdee)
            session['tdee_food'] = round(session['tdee_food'],1)
            session['limit_cal'] = limit_cal
            session['bmi_status'] = bmi_status
            session['callimit'] = result_tdee
            #session สำหรับทำงานหน้า Foods
            session['forlist'] = False
            session['sumcal'] = 0
            session['foods'] = list()
            session['foodscal'] = list()
            return render_template("result.html",tdee_des=bmi_tdee_des)

@app.route('/foods',methods=['GET','POST'])
def foodscal():
    name = food = foodcal = sumcal = countfoods = False

    if not session['name']:
        return redirect('/')

    callimit = float()
    foods=data.foods
    if request.method == 'POST':
        session['forlist'] = name
        if request.form['submit'] == 'ส่งข้อมูล':
            food = request.form['food']

            session['foods'].append(foods[food]['name'])
            session['foodscal'].append(foods[food]['cal'])

            session['callimit'] = session['callimit'] - foods[food]['cal']

        if request.form['submit'] == 'ส่งข้อมูลกำหนดเอง':
            food = request.form['food']
            foodcal = int(request.form['foodcal'])

            session['foods'].append(food)
            session['foodscal'].append(foodcal)

        if request.form['submit'] == 'ลบข้อมูลล่าสุด':
            session['foods'].pop()
            session['foodscal'].pop()

    countfoods = len(session['foods'])

    for i in session['foodscal']:
        sumcal = sumcal+i
    
    session['sumcal']=sumcal
    callimit = session['tdee_food']-sumcal
    callimit = round(callimit,1)
    chackcallimit = callimit
    if chackcallimit < 0:
        callimit = str(callimit).replace('-','')
        callimit = float(callimit)

    return render_template("foods.html",menu=foods,c=countfoods,s=sumcal,climit=callimit,cklimit=chackcallimit)

@app.route('/conclusion',methods=['GET','POST'])
def advise():
    bmi=session['bmi']
    limit=int(session['tdee_food'])
    sum=session['sumcal']
    if sum == False:
        sum = 0
    consult_de=fn.consult_des(bmi)
    consult_de=data.CON[consult_de]
    
    adv=fn.consult(sum,limit)
    adv=data.AD[adv]
    callimit=session['callimit']

    return render_template("conclusion.html",climit=callimit,t=sum,adv=adv,lim=limit,de=consult_de)

@app.route('/logout')
def logout():
    session['name'] = session['bmi'] = session['bmr'] = session['tdee'] = session['tdee_food'] = session['limit_cal'] = session['bmi_status'] = session['callimit'] = session['forlist'] = session['sumcal'] = session['foods'] = session['foodscal'] = None
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)