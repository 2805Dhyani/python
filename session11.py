Total_chores = 4
Orignal_num = 1
total_num = 4
Orignal_num = Total_chores

print (f"You {Orignal_num} to finish Today\n")

complete_count = 0
chore_num = 1

while chore_num <= total_num:
    if chore_num == 1 :next_chore = "Make your Bed"
    elif chore_num == 2:next_chore = "Wash Dirty Clothes"
    elif chore_num == 3:next_chore = "Play with your pet"
    else: next_chore = "Do your homework"

    answer = input(f"Have you finished {next_chore}? (yes/no):")

    if answer == "yes":
        complete_count += 1
        chore_num += 1
        print("Good job ! Chore completed ")
    else : print("Finish it ")

    print("chores remaing:", Total_chores - completed_count)
    print()

    print("=====All Chores Completed =====")
    print("Great work completed entire cheacklist today\n")

    print("Now lets safely peek at an infinite loop ...")
    test_value = 0
    safely_counter = 0
    while test_value <= 0 :
        print("This condition never changes, so this would run forever")
        safely_counter += 1
        if safely_counter == 3:
            print(("Stopping here on purpose -  is a real infinite loop never stops on it own !"))

            break

    print("\n ===== Chores Summary =====")
    print("Chore Assigned : Origanals_num")
    print("Chore completed : Completed_chore")
    print("Chore remaing :" , Total_chores - complete_count)






    


