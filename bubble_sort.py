# BUBBLE SORT
# - compare two adjacent elements
# - if first > second, swap
# - if first < second, leave as is
# - repeat steps excluding the sorted larger elements in the left part of the array

# unsorted list of numbers
numbers = [57, 81, 45, 44, 82, 76, 26, 48, 67, 12]
print(f"\nUnsorted numbers: {numbers}\n")

def bubbleSort(numbers):
    for element in range(len(numbers)-1, 0, -1): # external for loop for iterating elements from last to first position