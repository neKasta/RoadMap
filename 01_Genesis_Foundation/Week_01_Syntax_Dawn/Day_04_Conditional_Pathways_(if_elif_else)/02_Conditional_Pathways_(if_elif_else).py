stars = int(input())
money = int(input())
price = 135

if stars > 4 and money > price:
    print("Are you suitable")
elif stars < 4 and money > price:
    print("You are suitable, but with a caveat")
else:
    print("You are not suitable")
