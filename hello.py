raw_name = " 4na CRUZ "
clean_name = raw_name.strip().title()
print(clean_name)

temp = int(input("Reading temp is: "))

if temp <= 36:
    print("Temp is normal!")
elif temp >=37:
    print("Temp is hot!")
while temp!=0:
    break