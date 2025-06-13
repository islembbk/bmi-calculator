name = input("Hello, may I ask you about you name?")
print("hello", name )
age = int(input(" I'm curios about your age")) 
if age >= 20: print("too old") 
else: print("sup kiddo")
height = float(input("may I know your hieght 'cm'"))

if height >= 175: print("not bad ;) ")
else: print("sup shawty")
weight = float(input("Do you mind telling me your weight (in kgs)"))
height_m = height / 100
BMI= weight / (height_m ** 2)
BMI=round(BMI, 2)
print( name , "your BMI is" , BMI) 
if BMI < 18.5 : print("skinny nigga go eat something")
elif 18.5 <= BMI < 25 : print("keep it up,", name, "just don't lose it")
elif 25 <= BMI < 30 : print("DANGER DANGER", name, "YOU'RE GOING TO BE OBES")

else: print("u soo fat", name, ) 





























































































































