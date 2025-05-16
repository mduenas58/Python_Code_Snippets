x = []
y = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
x.append([row[i] for row in y for i in range(3)])  # SyntaxError: Unmatched bracket
print(x)
