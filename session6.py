field1 = 120
field2 = 95
field3 = 85
field4 = 150
field5 = 110

total = field1 + field2 + field3 + field4 + field5
avrage = total / 5

print("total harvest :" , total , "kg" )
print("avrage_per_feet :", avrage , "kg" )

price_per_kg = 15
earnings = total * price_per_kg

print("total earnings : Rs." , earnings)

bags = total // 25
leftover = total % 25

print("full bags packed :" , bags)
print("lefover grain :" , leftover , "kg")

last_year = 500
print("Better than last year ? :" , total > last_year)
print("Same as last year ? :", total == last_year)
print("At Least as good? :" , total>= last_year )

total += 30
print("After bonus crops :", total, "kg")

total -= 15
print("After seed reserve :" , total, "kg")

bags = total // 25
print("Final bags packed :" , bags)