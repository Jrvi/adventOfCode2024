left = []
right = []
distance = 0

# splits numbers to left and right arrays
with open("numbers.txt", encoding="utf-8") as f:
    content = f.read()
    t = content.split("\n")
    
    for line in t:
        s = line.split("   ")
        left.append(s[0]) 
        right.append(s[1])
    f.close()

# Sorting
left = sorted(left)
right = sorted(right)

# finding distance
for i in range(0, len(left)):
    d = int(left[i]) - int(right[i])
    if d < 0:
        d = d * -1
    distance = distance + d

print(f"total distance: {distance}")