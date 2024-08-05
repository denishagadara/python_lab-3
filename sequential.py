def sequential_search(elements, target):
    for index, value in enumerate(elements):
        if value == target:
            return index
    return -1

elements = [1, 3, 5, 8, 10, 23, 35]

target = 10

index = sequential_search(elements, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found.")

