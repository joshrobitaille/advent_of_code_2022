plays = []

input = open('reference/Day02/input.txt', 'r')
lines = input.read().splitlines()

def score(play:list[str]) -> int:
    opponent = play[0]
    self = play[1]
    points = 0

    if self == "X":
        points = 1
    if self == "Y":
        points = 2
    if self == "Z":
        points = 3

    match opponent:
        case "A":
            match self:
                case "X":
                    # print("draw")
                    points +=3
                case "Y":
                    # print("won")
                    points +=6
                case "Z":
                    # print("lost")
                    points +=0
        case "B":
            match self:
                case "X":
                    # print("lost")
                    points +=0
                case "Y":
                    # print("draw")
                    points +=3
                case "Z":
                    # print("won")
                    points +=6
        case "C":
            match self:
                case "X":
                    # print("won")
                    points +=6
                case "Y":
                    # print("lost")
                    points +=0
                case "Z":
                    # print("draw")
                    points +=3
    return points

for i in lines:
    plays.append(i.split())

totalScore = 0
for j in plays:
    totalScore += score(j)

print(totalScore)