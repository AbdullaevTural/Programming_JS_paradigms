def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
array = [1, 2, 3, 4, 5, 6, 7]

print(f"Исходный массив: {array}")
target = int(input("Введите искомый элемент: "))

result = binary_search(array, target)
if result == -1:
    print("Искомый элемент не найден")
else:
    print(f"Искомый элемент: {target} найден по индексу: {result}")