def Points(points):
    total_time = 0
    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        total_time += max(dx, dy)
    return total_time

raw_input = input("Points = ")

points = []
num = ''
pair = []
inside_brackets = False

for ch in raw_input:
    if ch == '[':
        pair = []
        inside_brackets = True
    elif ch == ',' and inside_brackets:
        pair.append(int(num.strip()))
        num = ''
    elif ch == ']':
        if num:
            pair.append(int(num.strip()))
            num = ''
        if pair:
            points.append(pair)
        inside_brackets = False
    elif ch.isdigit() or ch == '-' or ch == ' ':
        num += ch

result = Points(points)

print(result)
