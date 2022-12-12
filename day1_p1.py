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

print(max(totalCalories))

# elfNumber = 1
# for j in totalCalories:
#     print(f"elf {elfNumber} : {j}")
#     elfNumber += 1