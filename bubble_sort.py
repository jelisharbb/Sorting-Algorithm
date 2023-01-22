# BUBBLE SORT
# - compare two adjacent elements
# - if first > second, swap
# - if first < second, leave as is
# - repeat steps excluding the sorted larger elements in the right part of the array

# unsorted list of numbers
numbers = [57, 81, 45, 44, 82, 76, 26, 48, 67, 12]
print(f"\nUnsorted numbers: {numbers}\n")

def bubbleSort(numbers):

    for element in range(len(numbers)-1, 0, -1): # external for loop for iterating elements from last to first position
        for maxNum in range(element):
            if numbers[maxNum] > numbers[maxNum + 1]: # if statement for comparing the two adjacent elements

                # swapping of numbers
                tempNum = numbers[maxNum] # large number will be temporarily stored in a variable
                numbers[maxNum] = numbers[maxNum + 1] # the smaller number will be placed in the previous position of larger number
                numbers[maxNum + 1] = tempNum # the larger number will now be stored in the previous position of the smaller number

        print(numbers) # prints the numbers per loop
    
    print(f"\nSorted numbers: {numbers}\n")

bubbleSort(numbers)