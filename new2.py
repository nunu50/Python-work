name = input("what is your name? ")
school = input("which school do you learn? ")
place = input("where do you live? ")
birth_year = input("ok, great. tell me your birth year? not date, i said year.right? ")
year = int(2022) - int(birth_year)
print("ok thanks for giving information "+name+" you are "+str(year)+" years old.\n and you live in "+place+" that is the beautifull place. and \nyou learn in "+school+" that is great. hope you are doing well.bye!!!")
weight = int(input("please, enter your weight:"))
if weight < 30:
    print("you should eat more")
    print("that's not enough")
elif weight < 50:
    print("you have a balanced weight")
elif weight > 40:
    print("you have a unbalanced weight")
else:
    print("you are not feeling well")
