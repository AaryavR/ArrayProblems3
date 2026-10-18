def max_ones(n):
    arr = [1]*n + [0] + [1]*n
    streak = best = 0
    for x in arr:
        if x: streak +=1
        else: streak = 0
        if streak > best: best = streak
    return best

input("Max_ones(n) finds the longest run of 1s in [1..1, 0, 1..1]. Press enter")
print("max_ones(3)  = ", max_ones(3))
n = int(input("Enter n: ")) 
print(f"max_ones({str(n)}) = {max_ones(n)}")