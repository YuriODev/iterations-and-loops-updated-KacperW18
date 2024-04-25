# Your solution to Exercise 32
num_of_cars = int(input())
total = 0
slowest = 0
highest = 0
for i in range(num_of_cars):
    if i == 0:
        speed = int(input())
        highest = speed
        slowest = speed
    else:
        speed = int(input())
        if speed > highest:
            highest = speed
        if speed < slowest:
            slowest = speed
    if speed < 30:
        total += 1
print(highest - slowest)
print(total)