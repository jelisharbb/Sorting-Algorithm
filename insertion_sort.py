# INSERTION SORT
# - assume first element is sorted and the rest is unsorted
# - pick the first element in the unsorted part and place it in its correction position in the sorted part
# - repeat the steps

# unsorted list of numbers
numbers = [57, 81, 45, 44, 82, 76, 26, 48, 67, 12]
print(f"\nUnsorted numbers: {numbers}\n")

def insertionSort(numbers):

    for element in range(1, len(numbers)): # for loop that will traverse the unsorted part of the list
        currentNum = element # stored the number temporarily in the variable in order to place it in its right position in the sorted part of the list

        while numbers[currentNum - 1] > numbers[currentNum] and currentNum > 0: # while loop for comparing the 1st element in the unsorted part with the numbers in the sorted part