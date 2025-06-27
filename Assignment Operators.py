print("Assignment Operators")

#1. Start with a variable x = 0 and apply +=, -=, *=, /=, %=, step by step
x = 0
print("Initial x:", x)

x += 5
print("After += 5:", x)

x -= 2
print("After -= 2:", x)

x *= 3
print("After *= 3:", x)

x /= 2
print("After /= 2:", x)

x %= 4
print("After %= 4:", x)

#2. Create a counter that increases by 2 on each step, using `+=`
print("Counter increases by 2:")

counter = 0
for i in range(5):
    counter += 2
    print(counter)

#3. Create a simple savings balance calculator: add interest using '*='
balance = 100
interest_rate = 1.10  #Interest rate: 10%

balance *= interest_rate
print(f"Updated balance after 10% interest: {balance}")


#4. Simulate a countdown where each step decreases by using `-=`
print("countdown where each step decreases by :")

countdown= 5
for i in range(5):
    print("Countdown:", countdown)
    countdown -= 1

