Weight = int(input('enter your weight(kg) : '))
height = float(input('enter your height(m) : '))

BMI = Weight/(height*height)

if BMI < 18.5 :
    print('Underweight !')
if (18.5 < BMI) and (BMI < 24.9) : 
    print('Normal !') 
if (25 < BMI) and (BMI <  29.9) :
    print('Overweight !')
if (30 < BMI) and (BMI < 34.9) :
    print('Obese !')
if BMI > 35 :
    print('Exteremly obese !!!!')    
