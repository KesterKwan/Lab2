print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
import statistics
temp=[]
time=True
minmax=[]

def display_main_menu():
    print("display_main_menu")

def get_user_input(temp):
    time=True
   
    while time:
        tempinput=float(input("What is the temp? "))
        temp.append(tempinput)
        
        con=input("Do you wish to continue(Y/N)? ")
        if con == 'Y':
            time=True
        else:
            time=False

def calc_average():
    print("calc_average")
    xs=sum(temp)
    x=len(temp)
    avg=xs/x
    print("The average is", avg)

def find_min_max():
    minmax.append(min(temp))
    minmax.append(max(temp))
    print("The lowest and highest temp are:",minmax)

                  
def sort_temperature():
    temp.sort()
    print("Accending order is:",temp)

def calc_median_temperature():
    statistics.median(temp)
    print("The median is",statistics.median(temp))

    

        


        

       
        



def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input(temp)
    print(temp)
    calc_average()
    find_min_max()
    sort_temperature()
    calc_median_temperature()
    



if __name__ == "__main__":
    main()