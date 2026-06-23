
def add(x,y) :
    return x + y

def subtract(x,y) :
    return x - y

def multiply(x,y) :
    return x * y

def divide(x,y) :
    if x == 0 :
        return "Cannot Divie with 0!"
    else: x / y

def calculator():

    print("===The Calculator===")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - to Quit")
while True :

    calculator()

    cmd = input("Select Process To Execute: ")

    if cmd == '1' :
        d_one = float(input("Input value for x: "))
        d_two = float(input("Input value for y: ")) 
        total = d_one + d_two
        print (total)
    elif cmd == '2' :
        d_one = float(input("Input value for x: "))
        d_two = float(input("Input value for y: ")) 
        total = d_one - d_two
        print (total)
    elif cmd == '3' :
        d_one = float(input("Input value for x: "))
        d_two = float(input("Input value for y: ")) 
        total = d_one * d_two
        print (total)
    elif cmd == '4' :
        d_one = float(input("Input value for x: "))
        d_two = float(input("Input value for y: ")) 
        total = d_one / d_two
        print (total)
    elif cmd =='5' :
        break   
    else:
        print("Invalid choice. Please Try Again!")
