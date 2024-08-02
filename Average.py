chemistry = input("Enter your chemistry marks in 100 ")
biology = input("Enter your biology marks in 100 ")
physics = input("Enter your physics marks in 100 ")
english = input("Enter your english marks in 100 ")
maths = input("Enter your maths marks in 100 ")
AGRI = input("Enter your agriculture marks in 100 ")
ICT = input("Enter your ICT marks in 100 ")
Total = float(chemistry)+float(biology)+float(physics)+float(maths)+float(english)+float(ICT)+float(AGRI)
print(Total/7)
if (95 > Total):
    print("your marks are low! study hard")
elif(95>Total and 90<Total):
    print("meh! is good 😒")
else:
    print("KEEP IT UP!!! 🔥🔥🔥")