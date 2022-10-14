def bmi(weight, height):
    bmi_result = False
    bmi_result = float(weight)/(float(height)/100)**2
    bmi_result = round(bmi_result, 2)
    return bmi_result

def bmr(weight, height, age, gender):
    bmr_result = False
    if gender == 'men':
        bmr_result = 66 + (13.7*float(weight)) + (5*float(height)) - (6.8*int(age))
        bmr_result = round(bmr_result, 1)
        return bmr_result
    if gender == 'famale':
        bmr_result = 665 + (9.6*float(weight)) + (1.8*float(height)) - (4.7*int(age))
        bmr_result = round(bmr_result, 1)
        return bmr_result

def bmi_status(bmi):
    if bmi < 17.5:
        return 'thin3'
    if bmi >= 17.5 and bmi < 18:
        return 'thin2'
    if bmi >= 18 and bmi < 18.5:
        return 'thin'
    if bmi >= 18.5 and bmi < 24:
        return 'good'
    if bmi >= 24 and bmi < 25:
        return 'fat'
    if bmi >= 25 and bmi < 29:
        return 'fat1'
    if bmi >= 29 and bmi < 30:
        return 'fat2'
    if bmi >= 30:
        return 'fat3'

def tdee(tdee_input ,bmr):
    result_tdee = False
    if tdee_input == 'nowo':
        result_tdee = bmr*1.2
    if tdee_input == 'wo1':
        result_tdee = bmr*1.375
    if tdee_input == 'wo2':
        result_tdee = bmr*1.55
    if tdee_input == 'wo3':
        result_tdee = bmr*1.725
    if tdee_input == 'wo4':
        result_tdee = bmr*1.9
    result_tdee = round(result_tdee, 1)
    return result_tdee

def bmr_des(bmi, tdee):
    result = float()
    des = ''
    if bmi == 'thin' or bmi == 'thin2' or bmi == 'thin3':
        result = tdee+500
        des = 'หากคุณต้องการเพิ่มน้ำหนักให้รับพลังงานไม่เกิน {:.1f} (Kcal)'.format(result)
        return des
    if bmi == 'fat' or bmi == 'fat1' or bmi == 'fat2' or bmi == 'fat3':
        result = tdee-500
        return 'หากคุณต้องการลดน้ำหนักให้รับพลังงานไม่เกิน {:.1f} (Kcal)'.format(result)
    if bmi == 'good':
        return 'ร่างกายคุณอยู่ในสภาวะสมดุล คุณควรรักษาสมดุลร่างกายโดยรับพลังตามที่ร่างกายต้องการ'

def tdee_food(bmi, tdee):
    result = float()
    if bmi == 'thin' or bmi == 'thin2' or bmi == 'thin3':
        result = tdee+500
        return result
    if bmi == 'fat' or bmi == 'fat1' or bmi == 'fat2' or bmi == 'fat3':
        result = tdee-500
        return result
    if bmi == 'good':
        result = tdee
        return result

def consult(sum,limit): 
    if sum < limit-500:
        return 'วันนี้คุณรับประทานอาหารต่ำกว่ากำหนด ถ้าหากคุณต้องการเพิ่มน้ำหนักควรรับประทานอาหารให้อยู่ในช่วงแคลอรี่ของคุณและต้องมากกว่า {} Kcal และไม่ควรมากจนเกินไป'.format(limit)
    if sum > limit:
        return 'วันนี้คุณรับประทานอาหารเกินปริมาณแคลอรี่ที่ต้องการต่อวันแล้ว (แต่ถ้าหากว่าคุณต้องการลดน้ำหนัก คุณควรรับประทานให้อยู่ในช่วง {} Kcal - {} Kcal'.format(limit-500,limit)
    if sum <= limit and sum >= limit-500:
        return 'วันนี้คุณได้รับปริมาณพลังงานอยู่ในช่วงที่เหมาะสมต่อร่างกายแล้ว'

def consult_des(bmi):
    if bmi >= 17.5 and bmi <18.5:
        return 't'
    if bmi < 17.5:
        return 't-danger'
    if bmi >= 18.5 and bmi < 24:
        return 'g'
    if bmi >= 24 and bmi < 30:
        return 'f'
    if bmi >= 30:
        return 'f-danger'