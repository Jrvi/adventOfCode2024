import re

def mul(numbers):
    add = int(numbers[0]) * int(numbers[1])
    return add

with open("input.txt", encoding="utf-8") as f:
    content = f.read()
    regex = "mul\((\d{1,3}),(\d{1,3})\)"
    a = re.findall(regex, content)
    total = sum(mul(pair) for pair in a)

print(f"total: {total}")