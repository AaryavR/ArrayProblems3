arr = [1]*6 + [0]*4 + [1]*12

def max_ones():
    streak = best = 0
    for x in arr:
        if x: streak +=1
        else: streak = 0
        if streak > best: best = streak
    return best

print(f"max_ones() = {max_ones()}")

def move_zeros():
    write = 0
    for x in arr:
        if x: arr[write] = x; write += 1
    arr[write:] = [0] * (len(arr) - write)
    return arr


print(f"move_zeros() = {move_zeros()}")