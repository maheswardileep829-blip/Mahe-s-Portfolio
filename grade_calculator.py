print("-" * 40)
print("GRADE CALCULATOR")
print("-" * 40)


number_of_classes = int(input("How many classes?"))
print()

for i in range (number_of_classes):
    print (f"\n--- Class {1 + i} ---")

    name_of_class = input("What is the name of the class (Press enter to skip:)")

    if name_of_class == "":
     name_of_class = "your class"
    current_grade = float(input("What is your current grade in the class?"))
    desired_grade = float(input("What is your desired grade in the class?"))
    weight_final = float(input("How much is your final weighed in the class? (%)"))

    real_weight_final = weight_final / 100
    needed_grade = (desired_grade - (current_grade * (1 - real_weight_final))) / real_weight_final

    print (f'The grade you need to get in the final of {name_of_class} is {round (needed_grade, 1)}%')

    if needed_grade > 100:
    print ("You can not acheive your desired grade unless you have extra credit")
    elif needed_grade < 65:
    print ("All you gotta do is not fail")
    else: 
    print ("Study well and you got a shot")
