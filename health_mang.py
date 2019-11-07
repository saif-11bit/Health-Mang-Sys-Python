
import datetime

def time():
    return datetime.datetime.now()

def saif():
    if input_lock==0:
        if input_req=="e":
            input_msg = input("Enter your message: ")
            with open("saif_exer.txt", "a") as f:
                f.write("\n"+input_msg +  str([str(time())]))
                print("Done!")
        elif input_req=="f":
            input_msg = input("Enter your message: ")
            with open("saif_food.txt", "a") as f:
                f.write("\n"+input_msg +  str([str(time())]))
                print("Done!")
    elif input_lock==1:
        if input_req=="e":
            with open("saif_exer.txt") as f:
                f=f.read()
                print(f)
        elif input_req=="f":
            with open("saif_food.txt") as f:
                f=f.read()
                print(f)

def anas():
    if input_lock==0:
        if input_req=="e":
            input_msg = input("Enter your message: ")
            with open("anas_exer.txt", "a") as f:
                f.write("\n"+input_msg + str([str(time())]))
                print("Done!")
        elif input_req=="f":
            input_msg = input("Enter your message: ")
            with open("anas_food.txt", "a") as f:
                f.write("\n"+input_msg + str([str(time())]))
                print("Done!")
    elif input_lock==1:
        if input_req=="e":
            with open("anas_exer.txt") as f:
                f=f.read()
                print(f)
        elif input_req=="f":
            with open("anas_food.txt") as f:
                f=f.read()
                print(f)

def adil():
    if input_lock==0:
        if input_req=="e":
            input_msg = input("Enter your message: ")
            with open("adil_exer.txt", "a") as f:
                f.write("\n"+input_msg + str([str(time())]))
                print("Done!")
        elif input_req=="f":
            input_msg = input("Enter your message: ")
            with open("adil_food.txt", "a") as f:
                f.write("\n"+input_msg + str([str(time())]))
                print("Done!")
    elif input_lock==1:
        if input_req=="e":
            with open("adil_exer.txt") as f:
                f=f.read()
                print(f)
        elif input_req=="f":
            with open("adil_food.txt") as f:
                f=f.read()
                print(f)


if __name__ == "__main__":
    input_lock = int(input("lock(0) or retrive(1): "))
    input_name = input("name: ")
    input_req = input("exersice(e) or food(f): ")
    
    if input_name=="saif":
        saif()
    elif input_name=="anas":
        anas()
    elif input_name=="adil":
        adil()
        