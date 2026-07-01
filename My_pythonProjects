#how to calculate interest in python
principle = 0
rate = 0 
time = 0 
while True:
    principle = float(input("Enter the principle account "))
    if principle < 0:
        print ( "Princple can't less than   zero")
    else: 
        break

while True:
    rate = float(input("Enter the rate account "))
    if rate  < 0:
        print ( "rate  can't less than   zero")
    else:
        break

while True :
    time = int(input("Enter the time  in years  "))
    if time < 0:
        print ( "time can't less than   zero")
    else:
        break   


total = principle * pow((1 + rate/100), time)
print (f" Balance after {time} year/s: $ {total:.2f}")
