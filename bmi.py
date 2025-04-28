def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi=round(weight/(height * height),1)
    print("Bmi is",bmi)
    if bmi < 18.5:
        print("Under Weight")
    elif bmi >= 18.5 and bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")




calculate_bmi(weight=57, height=1.73)