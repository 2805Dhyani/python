name = input("Enter your Agent name ,Agent:")
gadget = input("Enter your gaget : ")

agent_number = 17
speed_rating = 9.5
mission_count = 26
height_m = 1.65
is_active = True

print("Name:",name,"-> type",type(name))
print("Gadget:",gadget,"-> type",type(gadget))
print("Agent number:",agent_number,"->type",type(agent_number))
print("Speed rating:",speed_rating,"->type",type(speed_rating))
print("Mission count:",mission_count,"->type",type(mission_count))
print("Height (m):",height_m,"->type",type(height_m))
print("Is Active:",is_active,"->type",type(is_active))

agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)

print("Agent number as text:",agent_number_text,"->type",type(agent_number_text))
print("Speed rating as text:",speed_rating_text,"->type",type(speed_rating_text))
print("Mission count as text:",mission_count_text,"->type",type(mission_count_text))
print("Status as text",status_text,"->type",type(status_text))

first_three = name[0:3:]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First 3 letters of name:",first_three)
print("last letter of name:",last_letter)
print("secreat code Name:",code_name)

reversed_gadget = gadget[::1]
print("Reversed Gadget Name:",reversed_gadget)

badge_line_1 = "AGENT" + code_name.upper()
badge_line_2 = "ID" + agent_number_text +"| MISSIONS:" + mission_count_text
badge_line_3 = "SPEED" + speed_rating_text +"| ACTIVE "+ status_text
badge_line_4 = "SECRET GAGET CODE" + reversed_gadget.upper()

print("")
print("===== SECRET AGENT BADGE =====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)

