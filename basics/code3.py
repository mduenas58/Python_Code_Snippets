x = []
y = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
x.append([item for row in y for item in row])  # Proper flattening
print(x)
