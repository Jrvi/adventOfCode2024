left = []
right = []
score = 0

# splits numbers to left and right arrays
with open("numbers.txt", encoding="utf-8") as f:
    content = f.read()
    t = content.split("\n")
    
    for line in t:
        s = line.split("   ")
        left.append(s[0]) 
        right.append(s[1])
    f.close()

# Sorting not needed
# left = sorted(left)
# right = sorted(right)

# finding score
for i in left:
    u = 0
    for j in right:
        if i == j:
            u = u + 1
    score = score + u * int(i)

print(f"total score: {score}")