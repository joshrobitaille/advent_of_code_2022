plays = []

input = open('reference/Day02/input.txt', 'r')
lines = input.read().splitlines()

def score(play:list[str]) -> int:
    opponent = play[0]
    self = play[1]
    points = 0

    match opponent:
        case "A":
            match self:
                case "X":
                    # need to lose (scissors) 
                    # loss = 0, scissors = 3
                    points = 3 
                case "Y":
                    # need to draw (rock) 
                    # draw = 3, rock = 1
                    points = 4
                case "Z":
                    # need to win (paper) 
                    # win = 6, paper = 2
                    points = 8
        case "B":
            match self:
                case "X":
                    # need to lose (rock)
                    # loss = 0, rock = 1
                    points = 1
                case "Y":
                    # need to draw (paper)
                    # draw = 3, paper = 2
                    points = 5
                case "Z":
                    # need to win (scissors)
                    # win = 6, scissors = 3
                    points = 9
        case "C":
            match self:
                case "X":
                    # need to lose (paper)
                    # loss = 0, paper = 2
                    points = 2
                case "Y":
                    # need to draw (scissors)
                    # draw = 3, scissors = 3
                    points = 6
                case "Z":
                    # need to win (rock)
                    # win = 6, rock = 1
                    points = 7
    return points

for i in lines:
    plays.append(i.split())

totalScore = 0
for j in plays:
    totalScore += score(j)

print(totalScore)