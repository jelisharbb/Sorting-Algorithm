# SELECTION SORT
# - find the smallest number
# - swap
# - repeat steps excluding the sorted smaller elements in the right

# unsorted array of numbers
numbers = [57, 81, 45, 44, 82, 76, 26, 48, 67, 12]
print(f"\nUnsorted numbers: {numbers}\n")

def selectionSort(numbers):
    for element in range(9): # for loop that will iterate over the numbers
        currentNum = element # current element will be stored in a variable for comparing
        for minNum in range(element, 10): # nested for loop for iterating again the numbers to be compared with the current number
            if numbers(minNum) < numbers(currentNum): # if condition to check if the iterated number is less than the current number 
                currentNum = minNum # the value of the current number will be replaced with the minimum number
        
        # swapping of numbers
        tempNum = numbers[element]
        numbers[element] = numbers[currentNum]
        numbers[currentNum] = tempNum