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
    if bmi < 16:
        return 'ผอมมากไป'
    if bmi >= 16 and bmi < 18:
        return 'ผอมพอสมควร'
    if bmi >= 18 and bmi < 18.6:
        return 'ผอม'
    if bmi >= 18.6 and bmi < 26:
        return 'good'
    if bmi >= 26 and bmi < 31:
        return 'น้ำหนักเกิน'
    if bmi >= 31 and bmi < 36:
        return 'น้ำหนักเกิน ระดับ 1'
    if bmi >= 46 and bmi < 41:
        return 'น้ำหนักเกิน ระดับ 2'
    if bmi > 40:
        return 'น้ำหนักเกิน ระดับ 3'

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