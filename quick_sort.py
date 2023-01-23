# QUICK SORT
# - choose any element as pivot
# - do 'partition': elements that are less than the pivot should be placed on the left side, while elements greater than the pivot should be placed on the right side
# - choose pivot element in the left side
# - do 'partition' again until all elements are sorted
# - choose pivot element in the right side
# - do 'partition' again until all elements are sorted

# unsorted list of numbers
numbers = [57, 81, 45, 44, 82, 76, 26, 48, 67, 12]
print(f"\nUnsorted numbers: {numbers}\n")

def quickSort(numbers, left, right):
    if left < right:
        partitionPos = partition(numbers, left, right)
        quickSort(numbers, left, partitionPos - 1) # recursion of sorting from leftmost index to the number before the pivot
        quickSort(numbers, partitionPos + 1, right) # recursion of sorting from the number after the pivot to the last element

def partition(numbers, left, right):

    # for tracking of indices
    leftIndex = left
    rightIndex = right
    pivotIndex = numbers[right]