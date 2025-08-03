width = 17
height = 12.0

expressions = [
    ("widht // 2", width // 2),
    ("width / 2.0", width / 2.0),
    ("height / 3", height / 3),
    ("1 + 2 * 5", 1 + 2 * 5),
]

for desc, result in expressions:
    print(f"{desc:12} → Value: {result:6} Type: {type(result).__name__}")