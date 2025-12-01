import math

# This code calculates the time and displacement given the intial y, v, and angle in degrees
while(True):
    y = float(input("\nEnter y displacement: "))
    v = float(input("Enter intial v: "))
    angle = math.radians(int(input("Enter lanch angle: ")))

    vy = v*math.sin(angle)
    time = (vy + math.sqrt(math.pow(vy, 2)+2*(9.8)*y))/9.8

    print("\nt = " + str(round(time, 3)) + "s")

    x = v*math.cos(angle)*time

    print("Predicted x is " + str(round(x, 3)) + "m")
