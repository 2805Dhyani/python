temperature = int(input("The temperature in celsius :"))

temperature = 15
if temperature < 20:
    outfit = "Jacket"
    print("Too cold ") 
    print("Wear a :", outfit)

else:
    outfit = "T-shirt"
    print("its hot outside")
    print("wear a :" , outfit)

is_raining = "yes:"
print("Bring A umbrella")

wind_speed = int(input("Enter today's wind_speed in km : "))
if wind_speed < 30:
    needs_windbreaker = "yes :"
    print("Too windy")
    print("wear a windbreaker")

else : 
    print("it is clam today")
    print("No windbreaker for your outfit")

has_puddles = (input("Is there puddles on the ground?"))
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is muddy .")
    print("Wear", shoes)

else :
    shoes = "footwear"
    print("The ground doesn't has mud .")
    print("wear" , shoes)


 



    