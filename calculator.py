d_one = float(input("Input value for x: "))
d_two = float(input("Input value for y: "))

while True :
    cmd = input("Select Process to execute the numbers: (1:add 2:sub 3:multiply 4:divide Q:Quit)")
    if cmd == 'Q' or 'q':
        break
    elif cmd == '1' :
        total = d_one + d_two
        print (total)
    elif cmd == '2' :
        total = d_one - d_two
        print (total)
    elif cmd == '3' :
        total = d_one * d_two
        print (total)
    elif cmd == '4' :
        total = d_one / d_two
        print (total)
