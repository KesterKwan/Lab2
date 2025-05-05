def calculate_bmi(height, weight):
    print("Height = ", height)
    print("Weight = ", weight)

    bmi = round(weight / (height * height), 1)
    print("BMI is", bmi)
    return bmi 

def check_bmi(bmi):   
    if bmi < 18.5:
        return -1  
    elif 18.5 <= bmi <= 25:
        return 0   
    else:
        return 1

def main():
    height = float(input("What is your height (in metres)? "))
    weight = float(input("What is your weight (in kg)? "))

    bmi = calculate_bmi(height, weight)
    result = check_bmi(bmi)

    if result == -1:
        print("You are underweight.")
    elif result == 0:
        print("You have a normal weight.")
    else:
        print("You are overweight.")

if __name__ == "__main__":
    main()