def max_zeros(n):
    arr = [1] + [0]*n + [1]
    streak = best = 0
    for x in arr:
        if not x: streak +=1
        else: streak = 0
        if streak > best: best = streak
    return best

input("Max_zeros(n) finds the longest run of 1s in [1..1, 0, 1..1]. Press enter")
print("max_zeros(3)  = ", max_zeros(3))
n = int(input("Enter n: ")) 
print(f"max_zeros({str(n)}) = {max_zeros(n)}")