def is_safe_report(report):
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    is_diff_valid = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    return (is_increasing or is_decreasing) and is_diff_valid

def is_safe_with_dampener(report):
    if is_safe_report(report):
        return True
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report(modified_report):
            return True
    
    return False

with open("input.txt", encoding="utf-8") as f:
    content = f.read()
    reports = [list(map(int, line.split())) for line in content.strip().split("\n")]
    safe = sum(is_safe_with_dampener(report) for report in reports)

print(f"save: {safe}")