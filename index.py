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
    weight = height = gender = bmi_result = age = bmr_result = name = tdee = result_tdee = bmi_status = bmi_tdee_des = False
    #เก็บข้อมูลจากฟอร์มหน้าแรก
    if request.method == 'POST':
        name = request.form['name'] #เก็บชื่อ
        weight = request.form['weight'] #เก็บน้ำหนัก (กิโลกรัม)
        height = request.form['height'] #เก็บส่วนสูง (เซนติเมตร)
        age = request.form['age'] #เก็บอายุ
        gender = request.form['gender'] #เก็บเพศ men OR famale
        tdee = request.form['tdee'] #เก็บลักษณะการใช้ชีวิต

    try: #เช็ค Error
        bmi_result = fn.bmi(weight, height) #BMI Calulator เรียกใช้ฟังก์ชัน bmi เพื่อเก็บค่า BMI
        bmi_status = fn.bmi_status(bmi_result) #BMI Status เรียกใช้ฟังก์ชัน bmi_status เพื่อนำค่าไปหาเกณ์ BMI
        bmi_status = data.BMI[bmi_status] #เรียกใช้ data BMI เพื่อนำข้อมูลใน dirt มาใช้ ส่ง bmi_status เป็น key เพื่อที่จะเข้าถึงถึงข้อมูล status และ des(คำอธิบาย) ของเกณฑ์ BMI นั้น 
        
        bmr_result = fn.bmr(weight, height, age, gender) #BMR Calulator เรียกใช้ฟังก์ชัน bmr เพื่อเก็บค่า BMR

        result_tdee = fn.tdee(tdee, bmr_result) #เรียกใช้ฟังก์ชัน tdee เพื่อเก็บค่า TDEE
        bmi_tdee_des = fn.bmr_des(fn.bmi_status(bmi_result),result_tdee) #เรียกใช้ฟังก์ชัน bmr_des เพื่อเก็บข้อความให้คำแนะนำการลดหรือเพิ่มน้ำหนักให้อยู่เกณฑ์สมส่วน (ส่ง bmi_status และ ค่า TDEE ไปทำงาน)
    except ZeroDivisionError: #ถ้าเกิด Erorr ให้กลับหน้าแรก
        return redirect('/')
    else:
        #สร้าง Session เพื่อนำไปทำงานใน Templates
        session['name'] = name #ชื่อ
        session['bmi'] = bmi_result #ค่า BMI
        session['bmr'] = bmr_result #ค่า BMR
        session['tdee'] = result_tdee #ค่า TDEE
        session['tdee_des'] = bmi_tdee_des #คำแนะนำ เพิ่มหรือลดและสมส่วน
        session['tdee_food'] = fn.tdee_food(fn.bmi_status(bmi_result),result_tdee) #คำแนะนำในการรับพลังงานต่อวัน เรีกใช้ฟังก์ชัน tdee_food ส่ง bmi_status และ ค่า tdee ไปทำงาน (แสดงในหน้า foods)
        session['bmi_status'] = bmi_status  # drit ของ BMI Status (มี Key status, des)
        session['callimit'] = result_tdee # ค่า TDEE เพื่อนำไปทำงานในหน้า foods
        #session สำหรับทำงานหน้า Foods
        session['forlist'] = False
        session['sumcal'] = 0 #เพื่อเก็บผลรวมพลังงานการรับประทานอาหารทั้งหมด
        session['foods'] = list() #เพื่อเก็บชื่ออาหารที่รับประทานทั้งหมด
        session['foodscal'] = list() #เพื่อเก็บค่าพลังงานจากการรับประทานอาหารทั้งหมด
    return render_template("result.html")

@app.route('/foods',methods=['GET','POST'])
def foodscal():
    name = food = foodcal = sumcal = countfoods = False
    callimit = float() #เพื่อเก็บค่าพลังงานคงเหลือที่สามารถรับได้
    foods = data.foods #เก็บข้อมูลอาหารจาก Data และเข้าถึงข้อมูล foods
    if request.method == 'POST':
        session['forlist'] = name

        if request.form['submit'] == 'ส่งข้อมูล': #ถ้าส่งข้อมูลจากลิสต์อาหารที่มีอยู่แล้ว
            food = request.form['food'] #เก็บชื่ออาหารจากฟอร์ม (เป็น key จากข้อมูล data.foods)

            session['foods'].append(foods[food]['name']) #เพิ่มชื่ออาหาร
            session['foodscal'].append(foods[food]['cal']) #เพิ่มค่าพลังงาน


        if request.form['submit'] == 'ส่งข้อมูลกำหนดเอง': #ถ้าส่งข้อมูลแบบกำหนดเอง
            food = request.form['food'] #เก็บชื่ออาหารจากฟอร์ม
            foodcal = int(request.form['foodcal']) #เก็บค่าพลังงานจากฟอร์ม

            session['foods'].append(food) #เพิ่มชื่ออาหาร
            session['foodscal'].append(foodcal) #เพิ่มค่าพลังงาน

        if request.form['submit'] == 'ลบข้อมูลล่าสุด': #ถ้าลบข้อมูลล่าสุด
            session['foods'].pop() #ลบข้อมูลจาก list
            session['foodscal'].pop() 
    
    try: #เช็ค Erorr
        countfoods = len(session['foods'])  #เก็บจำนวนข้อมูลใน list
    except TypeError: #ถ้าเกิด Erorr ให้กลับหน้าแรก
        return redirect('/')

    for i in session['foodscal']: #Loop เพื่อดึงค่าออกมา
        sumcal = sumcal+i #เพิ่มค่าลง sumcal
    
    session['sumcal'] = sumcal #สร้าง session เก็บค่า sumcal

    callimit = session['tdee_food'] - sumcal #เก็บค่าพลังงานคงเหลือ โดย tdee_food ลบ ผลรวมพลังงานที่รับประทานไปทั้งหมด
    callimit = round(callimit,1) #ทำให้เป็นทศนิยม 1 ตำแหน่ง

    chackcallimit = callimit
    if chackcallimit < 0:
        callimit = str(callimit).replace('-','') #ถ้าพลังงานคงเหลือติดลบ เอาเครื่องหมายลบออก
        callimit = float(callimit)
    
    session['cllimit'] = callimit #สร้าง session เก็บค่า พลังงานคงเหลือ

    return render_template("foods.html",menu=foods,c=countfoods,cklimit=chackcallimit) #ส่งข้อมูลออกไปทำงานหน้า Template

@app.route('/conclusion',methods=['GET','POST'])
def advise():
    
    try:
        consult_de = fn.consult_des(session['bmi']) #เรียกใช้ฟังก์ชัน consult_des และเก็บค่า
        consult_de = data.CON[consult_de] #เรียกใช้ Data.CON เข้าถึงคีย์จาก consult_des
    except TypeError:
        return redirect('/')
    
    adv=fn.consult(session['sumcal'],session['tdee_food'],session['bmi'])

    session['consult'] = consult_de
    session['advice'] = adv

    return render_template("conclusion.html")

@app.route('/logout')
def logout():
    session['name'] = session['bmi'] = session['bmr'] = session['tdee'] = session['tdee_food'] = session['bmi_status'] = session['callimit'] = session['forlist'] = session['sumcal'] = session['foods'] = session['foodscal'] = session['consult'] = session['advice'] = session['cllimit'] = None
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)