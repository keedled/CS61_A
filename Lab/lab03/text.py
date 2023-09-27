def num_eights(x):
    if x == 0:
        return 0
    if x%10 == 8 :
        return 1 + num_eights(x//10)
    else :
        return num_eights(x//10)

def pingpong(n):
    def pingpong_help(index, sum, direction):
        if index == n:
            return sum

        if index % 8 == 0 or num_eights(index):
            if direction:
                return pingpong_help(index + 1, sum - 1, direction^1)
            else:
                return pingpong_help(index + 1, sum + 1, direction^1)

        if direction:
            return pingpong_help(index + 1, sum + 1, direction)
        else:
            return pingpong_help(index + 1, sum - 1, direction)

    return pingpong_help(1, 1, 1)

print(pingpong(23))