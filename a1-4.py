w=int(input('enter your weight(kg) : '))
h=float(input('enter your height(m) : '))

bmi=w/(h*h)

if bmi < 18.5 :
    print('Underweight !')
if (18.5 < bmi) and (bmi < 24.9) : 
    print('Normal !') 
if (25 < bmi) and (bmi <  29.9) :
    print('Overweight !')
if (30 < bmi) and (bmi < 34.9) :
    print('Obese !')
if bmi > 35 :
    print('Exteremly obese !!!!')    
