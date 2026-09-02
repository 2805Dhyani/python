print("Lets Make Your Vehical")

print("Pick your Vehical")
print("1 = Bike")
print("2 = Car")
print()

Choice = int(input("Enter your Choice"))
if Choice == 1 :
    print("1 = Scooty")
    print("2 = Mountain Bike")
    print()

    bike_type = int(input("Enter your bike type"))
    if bike_type == 1:
        print("You picked : Scooty")
        print("Top speed : 80km/h")
        print("Best for : city roads")

    else :

        print("You picked : Mountain bike")
        print("Top speed : 40km/h")
        print("Best for : road trip")

elif Choice == 2:
    print("1 = BMW")
    print("2 = Thar")
    print()

    car_type = int(input("Enter your car type"))
    if car_type == 1:
        print("You picked : BMW")
        print("Seats : 7 passengers")
        print("Best for : Family use")

    else :
        print("You picked : Thar " )
        print("seats : 4 passengers")
        print("Best for : Adevnature trips")

print("You Have Picked A Lovely Vehical")



