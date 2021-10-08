import sys
sys.setrecursionlimit(10000)

def get_probability(n, k):
    def f(order):
        if len(order) > n:
            return
        if len(order) == n:
            if 'A' * k not in order:
                possibilites.add(order)
        else:
            f(order + 'P')
            f(order + 'A')

    possibilites = set()
    ways_to_attend_graduation = 0
    f('')
    for possibility in possibilites:
        if possibility[-1] == 'A':
            ways_to_attend_graduation += 1
    return ways_to_attend_graduation, len(possibilites)

ways_to_attend_graduation, possibilites = get_probability(20, 4)
print(str(ways_to_attend_graduation) + "/" + str(possibilites))