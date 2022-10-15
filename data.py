#เก็บเกณฑ์ BMI และคำอธิบาย โดย mainKey อ้างอิงจาก function bmi_status
BMI = {
    "thin3":{
        'status':'ผอมต่ำกว่าเกณฑ์',
        'des':'อยู่ในเกณฑ์อันตรายต่อชีวิต ควรไปพบแพทย์โดยทันที เพื่อเข้ารับการตรวจร่างกายและรับการดูแลโดยผู้เชี่ยวชาญ รักษาระดับโปรตีนในร่างกาย เพื่อลดความเสี่ยงต่อโรคขาดสารอาหาร เมื่อรักษาระดับได้แล้วควรออกกำลังกายอย่างเคร่งครัด'
    },
    "thin2":{
        'status': 'ผอมพอสมควร',
        'des':'เริ่มเสี่ยงที่จะเป็นโรคผอม ควรไปปรึกษาแพทย์เพื่อรับคำแนะนำ เพื่อหลีกเลี่ยงความเสี่ยงที่จะเป็นโรคร้ายแรง ออกกำลังกายเพื่อสร้างกล้ามเนื้อ รับประทานอาหารที่ให้พลังงานที่มากพอที่จะออกกำลังกายได้'
    },
    "thin":{
        'status':'ผอม',
        'des':'อยู่ในเกณฑ์เริ่มผอม ควรเริ่มดูแลสุขภาพ เพื่อรักษาเกณฑ์ของตัวเองให้อยู่ในเกณฑ์สมส่วน หลีกเลี่ยงโรคผอมและโรคอื่นที่จะตามมาได้'
    },
    "good":{
        'status':'สมส่วน',
        'des':'จัดอยู่ในเกณฑ์ปกติ ห่างไกลโรคที่เกิดจากความอ้วน และมีความเสี่ยงต่อการเกิดโรคต่าง ๆ น้อยที่สุด ควรพยายามรักษาระดับค่า BMI ให้อยู่ในระดับนี้ให้นานที่สุด และควรตรวจสุขภาพทุกปี'
    },
    "fat":{
        'status':'น้ำหนักเกิน',
        'des':'น้ำหนักที่เหมาะสมสำหรับคนไทยคือค่า BMI ระหว่าง 18.5-24 จัดอยู่ในเกณฑ์ปกติ ห่างไกลโรคที่เกิดจากความอ้วน และมีความเสี่ยงต่อการเกิดโรคต่าง ๆ น้อยที่สุด ควรพยายามรักษาระดับค่า BMI ให้อยู่ในระดับนี้ให้นานที่สุด และควรตรวจสุขภาพทุกปี'
    },
    "fat1":{
        'status':'น้ำหนักเกิน ระดับ 1',
        'des':'อ้วนในระดับหนึ่ง ถึงแม้จะไม่ถึงเกณฑ์ที่ถือว่าอ้วนมาก ๆ แต่ก็ยังมีความเสี่ยงต่อการเกิดโรคที่มากับความอ้วนได้เช่นกัน ทั้งโรคเบาหวาน และความดันโลหิตสูง ควรปรับพฤติกรรมการทานอาหาร ออกกำลังกาย และตรวจสุขภาพ'
    },
    "fat2":{
        'status':'น้ำหนักเกิน ระดับ 2',
        'des':'ค่อนข้างอันตราย เสี่ยงต่อการเกิดโรคร้ายแรงที่แฝงมากับความอ้วน หากค่า BMI อยู่ในระดับนี้ จะต้องปรับพฤติกรรมการทานอาหาร และควรเริ่มออกกำลังกาย และหากเลขยิ่งสูงกว่า 40.0 ยิ่งแสดงถึงความอ้วนที่มากขึ้น ควรไปตรวจสุขภาพ และปรึกษาแพทย์'
    },
    "fat3":{
        'status':'น้ำหนักเกิน ระดับ 3',
        'des':'อันตรายต่อสุขภาพ ควรรีบไปพบแพทย์โดยด่วน เพื่อเข้ารับการตรวจสุขภาพทำให้แน่ใจว่าไม่มีโรคซ้อนและรับยาทันที่ ให้แพทย์นัดเวลาการตรวจเช็คสุขภาพและปฏิบัติตามคำแนะนำของแพทย์อย่างเคร่งครัดและรักษาระดับไขมันไม่ให้เกินเกณฑ์ของร่างกาย'
    }
}

#เก็บคำอธิบายสรุป
CON = {
    "t-danger":{'de':'ร่างกายของคุณตอนนี้อยู่ในความเสี่ยงต่อโรคร้ายที่จะทำให้คุณเสี่ยงต่อการใช้ชีวิตของคุณ คุณควรไปตรวจร่างกายจากแพทย์ การออกกำลังกายนั้นเป็นไปได้แต่ตารางการออกกำลังกายไม่ควรที่จะหนักเกินกว่าร่างกายของคุณจะรับไหว ควรได้รับการดูแลและคำแนะนำในขณะที่ออกกำลังกาย เพื่อไม่ให้หัวใจทำงานหนักจนเกินไป'
    },
    "t":{'de':'ร่างกายของคุณในตอนนี้นั้นมีน้ำหนักต่ำกว่าเกณฑ์แต่ยังไม่ถึงขั้นอันตรายมาก หากคุณเป็นคนที่สูงแต่น้ำหนักน้อยอาจเสี่ยงต่อการได้รับอาหารและพลังงานไม่เพียงพอ อย่างไรก็ตามหากคุณอยู่ในเกณฑ์นี้เราขอแนะนำให้รับประทานอาหารให้มากขึ้นแต่ก็ต้องระวังอย่าให้มากเกินไป และควรออกกำลังกายเพื่อสร้างกล้ามเนื้อ'
    },
    "g":{'de':'ระดับของคุณตอนนี้อยู่ในเกณฑ์ที่ดี ห่างไกลจากโรค คุณควรรักษาระดับของคุณให้อยู่ในเกณฑ์นี้ไว้ โดยการรับประทานอาหารตามจำนวนแคลอรี่ที่เราได้กำหนดไว้'
    },
    "f":{'de':'ตอนนี้ร่างกายของคุณอยู่ในระดับอ้วนหรือเริ่มอ้วนขึ้นแล้ว คุณควรรับประทานอาหารให้น้อยกว่า 1200 Kcal และจะส่งผลดีกับคุณหากครบ 5 หมู่ด้วย ลดปริมาณน้ำตาลเพื่อลดความเสี่ยงต่อการเป็นโรคเบาหวาน อย่างสุดท้ายคือคุณควรที่จะออกกำลังกายอย่างสม่ำเสมอ เพื่อนำปริมาณน้ำและไขมันในร่างกายของคุณออก'
    },
    "f-danger":{'de':'ร่างกายของคุณเสี่ยงต่อการเป็นโรคร้ายแรงที่ตามมากับโรคอ้วน เช่น โรคหลอดเลือดสมอง มะเร็งบางชนิด โรคหลอดเลือดหัวใจตีบหรือตัน เป็นต้น คุณควรไปปรึกษาแพทย์โดยเร็ว หลังจากนั้นควรปรับพฤติกรรมการทานอาหาร และออกกำลังกาย'
    }
}

#เก็บรายการอาหารและค่าพลังงานของอาหาร
foods = {
    "pantai":{
        "name":"ผัดไทย",
        "cal": 600
        },
    "padkapao":{
        "name":"ผัดกะเพรา",
        "cal": 561 
        },
    "chicken":{
        "name":"ข้าวมันไก่",
        "cal":695
        },
    "noodle":{
        "name":"ก๋วยเตี๋ยว ",
        "cal":450
        },
    "karee":{
        "name":"ผัดพงกะหรี่",
        "cal":746.1
        },
    "pad":{
        "name":"ข้าวผัด",
        "cal":163
        },
    "kaosoy":{
        "name":"ข้าวซอย",
        "cal":154
        },
    "kao-na-kai-yak":{
        "name":"ข้าวหน้าไก่ย่าง",
        "cal":397.5
        },
    "lummu":{
        "name":"ลาบหมู",
        "cal":130
        },
    "grilled pork":{
        "name":"หมูปิ้ง",
        "cal":94
    },
    "Sweet abd Sour stir Fry":{
        "name":"ผัดเปรี้ยวหวาน",
        "cal":116
    },
    "omelet":{
        "name":"ไข่เจียว  ",
        "cal":154
    },
    "Fried egg":{
        "name":"ไข่ดาว",
        "cal":90
    },
    "toasted eggs":{
        "name":"ไข่ปิ้ง",
        "cal":155
    },
    "lad nha":{
        "name":"ราดหน้า",
        "cal":609
    },
    "mango with stickyrice":{
        "name":"ข้าวเหนียวมะม่วง",
        "cal":450
    },
    "green curry":{
        "name":"แกงเขียวหวาน",
        "cal":95
    },
    "Massama curry":{
        "name":"แกงมัสมั่นไก่",
        "cal":252
    },
    "ramen":{
        "name":"ราเมง",
        "cal":436
    },
    "shrimp in fish sauce":{
        "name":"กุ้งแช่น้ำปลา 1 ตัว",
        "cal":14
    },
    "Pikled Crab with Fish sauce":{
        "name":"ปูดองน้ำปลา",
        "cal":500
    },
    "oil-chicken":{
        "name":"ไก่ทอดหาดใหญ่",
        "cal":246
    },
    "egg palo":{
        "name":"ไข่พะโล้",
        "cal":246
    },
    "bamboo curry":{
        "name":"แกงหน่อไม้",
        "cal":27
    },
    "egg son wife":{
        "name":"ไขลูกเขย",
        "cal":165
    },
    "pork hun":{
        "name":"หมูหั่น",
        "cal":376
    },
    "fish boil lemon":{
        "name":"ปลากระพงนึ่งมะนาว",
        "cal":140
    },
    "fried chicken":{
        "name":"ข้าวไก่กรอบ",
        "cal":693
    },
    "noodle and shirmp":{
        "name":"กุ้งอบวุ้นเส้น",
        "cal":300
    },
    "salt egg with pork":{
        "name":"หมูสับนึ่งไขเค็ม",
        "cal":315
    },
    "Burger and chick fried":{
        "name":"เบอร์เกอร์ไก่ทอด",
        "cal":628
    },
    "chilli hot dog":{
        "name":"ชิลลี่ฮอลดอก",
        "cal":271
    },
    "Duck Rice":{
        "name":"ข้าวหน้าเป็ด",
        "cal":495
    },
    "Pizza":{
        "name":"pizza",
        "cal":176
    },
    "red pog":{
        "name":"ข้าวหมูแดง",
        "cal":540
    },
    "pineapple curry":{
        "name":"แกงสัปปะรด",
        "cal":394.4
    },
    "wing zap":{
        "name":"วิงซ์แซ่บ",
        "cal":100
    },
    "chicken wing fried":{
        "name":"ปีกไก่ทอด",
        "cal":491
    },
    "Tariyagi burger":{
        "name":"เบอร์เกอร์ไก่เทอริยากิ",
        "cal":381
    },
    "chesse burger":{
        "name":"ชีสเบอร์เกอร์",
        "cal":300
    },
}