'''fp = open('samplelevel.lvl') # open file on read mode
bricks = fp.read().split("\n") # create a list containing all lines
print(bricks)
fp.close() # close file'''

with open("samplelevel.lvl") as f:
    bricks = f.read().splitlines()

f.close()

print(bricks)

for i in range(0, len(bricks)):
    bricks[i] = [int(j) for j in bricks[i].split()]
    print(bricks[i])

#bricks[0] = [int(x) for x in bricks[0].split()]

print(bricks)
