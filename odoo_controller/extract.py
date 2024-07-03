with open('copy_manifest', 'r') as file:
    data = file.read().rstrip()

data = eval(data)


if 'external_dependencies' in data:
    items = data["external_dependencies"]["python"]
    for item in items:
        print("pip install " + item)

