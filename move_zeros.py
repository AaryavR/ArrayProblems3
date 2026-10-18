def move_zeros(n):
    arr = [0, 1] * n
    write = 0
    for x in arr:
        if x: arr[write] = x; write += 1
    arr[write:] = [0] * (len(arr) - write)
    return arr

input("move_zeros(n) moves all zeros to the end of [0,1,0,1,0,1...]>. Press enter ")
print(" move_zeros(3) =", move_zeros(3))
n = int(input("Enter n:"))
print(f"move_zeros({str(n)}) = {move_zeros(n)}")
