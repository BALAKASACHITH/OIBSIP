#BMI(Body Mass Indes)Calculator OIBSIP
while True:
    try:
        weightInKilograms=float(input("Enter Your Weight in Kilograms : "))
        if weightInKilograms < 0:
            print("Please enter a non-negative value.")
        else:
            break
    except ValueError:
        print("Please enter a valid floating-point number.")
while True:
    try:
        heightInMeters=float(input("Enter You Height in Meters     : "))
        if heightInMeters < 0:
            print("Please enter a non-negative value.")
        else:
            break
    except ValueError:
        print("Please enter a valid floating-point number.")
BMI=(weightInKilograms)/(heightInMeters*heightInMeters)
BMI=round(BMI,2)
print("BMI                            :",BMI)
if BMI<18.5:
    print("Categorie                      : UnderWeight")
elif BMI>=18.5 and BMI<=24.9:
    print("Categorie                      : NormalWeight")
elif BMI>=25 and BMI<=29.9:
    print("Categorie                      : OverWeight")
else:
    print("Categorie                      : Obesity")
#<-------------------------------------THANK YOU !!------------------------------------------------------>