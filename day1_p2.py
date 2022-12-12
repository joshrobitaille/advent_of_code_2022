totalCalories = []

input = open('reference/Day01/input.txt', 'r')
lines = input.read().splitlines()

calorieCount = 0

for i in lines:
    if i == "":
        totalCalories.append(calorieCount)
        calorieCount = 0
    else:
        calorieCount += int(i)

topThree = sorted(totalCalories, reverse=True)[:3]

print(sum(topThree))