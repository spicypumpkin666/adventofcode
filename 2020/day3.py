import logging as log

log.basicConfig(level=log.DEBUG)

r = open('day3.txt').read().strip('\n')
trees = r.splitlines()

def traverse_trees(trees, rise, run):
    count = 0
    x = 0
    y = 0

    while True:
        y = y + rise
        if y >= len(trees):
            break
        x = (x + run) % len(trees[y])
        if trees[y][x] == '#':
            count+=1
    return count

oneone = traverse_trees(trees, 1, 1)
threeone = traverse_trees(trees, 1, 3)
fiveone = traverse_trees(trees, 1, 5)
sevenone = traverse_trees(trees, 1, 7)
onetwo = traverse_trees(trees, 2, 1)


log.info(f"traversed 1, 1: {oneone}")
log.info(f"traversed 3, 1: {threeone}")
log.info(f"traversed 5, 1: {fiveone}")
log.info(f"traversed 7, 1: {sevenone}")
log.info(f"traversed 1, 2: {onetwo}")

log.info(f"final num of trees: {oneone * threeone * fiveone * sevenone * onetwo}")
