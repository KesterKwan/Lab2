def calculate_bmi(height, weight):
    print("Height = " , height)
    print("Weight = " , weight)

    bmi=round(weight/(height * height),1)
    print("Bmi is",bmi)
    return bmi

def check_bmi(bmi):   
    if bmi < 18.5:
        print("Under Weight")
    elif bmi >= 18.5 and bmi <= 25.0:
        print("Normal Weight")
    else:
        print("Over Weight")


def main():

    height=float(input("What is your weight (in kg)? "))
    weight=float(input("What is your height (in metres)? "))
    calculate_bmi(weight ,height)
    check_bmi(bmi)




if __name__ == "__main__":main()