
numbers = [1,8,9,4,5,2,6,3,7];
def sort_numbers_descending(numbers):
    numbers.sort(reverse=True)
    return numbers

def sort_list_imperative(numbers): 
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
    return numbers




print(f"Declarative style -> {sort_numbers_descending(numbers)}")
print(f"Imperative style -> {sort_list_imperative(numbers)}")