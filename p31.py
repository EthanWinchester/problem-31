def problem31():
    possibilities = [[0, 0, 0, 0, 0, 0, 0, 0]]
    r_coins = [200, 100, 50, 20, 10, 5, 2, 1]
    n = []
    for i in r_coins:
        n.append(200 // i)
    for i in range(0, 8):
        tail = []
        for j in possibilities:
            value = 0
            for k in range(0, 8):
                value += j[k]*r_coins[k]
            left = 200 - value
            if left == 0:
                continue
            else:
                for k in range(0, left // r_coins[i]):
                    new = []
                    for l in range(0, 8):
                        new.append(j[l])
                    new[i] += k + 1
                    tail.append(new)
        for j in tail:
            possibilities.append(j)
    values_possible = []
    for i in possibilities:
        value = 0
        for j in range(0, 8):
            value += i[j]*r_coins[j]
        values_possible.append(value)
    result = 0
    for i in values_possible:
        if i == 200:
            result += 1
    print(values_possible)
    print(possibilities)
    print(len(possibilities))
    print(result)
    return result
