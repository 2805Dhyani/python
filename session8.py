print("=== SMART SCHOOL PLANNER ===")
print("I will ask quick 3 questions you have to answer it")

Day = input("What day is it?").strip().capitalize()
Weather = input("What weather is it?").strip().lower()
Homework = input("Is your homework done?").strip().lower()

if Day in("saturday" , "sunday"):
    print("Day type : weekend.Enjoy your day")

elif Day in("Monday"):
    print("Day type: First day of the week . go to school")

elif Day in("Friday"):
    print("Day type : last day of the week . Enjoy yor weekend")

elif Day in("Tuesday , Wednesday , Thursday"):
    print("Regular Day. Stay focused")

else:
    print("Day type : Day not recognisened . check spelling")

if Weather == "sunny" and Homework == "yes":
    print("Very good")

if Weather == "Rainy" or Weather == "Cloudy":
    print("Weather tip : Carry your umbrella")

if not (Homework == "yes"):
    print("complete and go")

if Weather == "Rainy" and not(Homework == "yes"):
    print("Its ok show it tomorrow")

elif Weather == "sunny" and Homework == "yes" and not (Day in("saturday" , "sunday")):
    print("give me your parents number")

else:
    print("Do the homwork everyday")

print()
print("HAVE A NICE DAY! Byee everyone")



     



