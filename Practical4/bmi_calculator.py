weight=float(input("Weight: (kg)")) #get your weight and height
height=float(input("height: (m)"))
BMI=weight/height**2  #calculate BMI


# output your BMI and catagory
if BMI>30:
    print("BMI:"+str(BMI),"  Obese")
elif BMI<18.5:
    print("BMI:"+str(BMI),"  Underweight")
else:
    print("BMI:"+str(BMI),"  Normal")