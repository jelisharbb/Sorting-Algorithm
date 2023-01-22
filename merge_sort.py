# MERGE SORT (divide and conquer algorithm)
# - divide array into left and right part

# - sort left by dividing it again into left and right part
# - keep dividing until it becomes single element only, making it sorted
# - merge the single left part with its other half (single right part)
# - keep merging until the original left part becomes sorted

# - sort right by dividing it again into left and right part
# - keep dividing until it becomes single element only, making it sorted
# - merge the single left part with its other half (single right part)
# - keep merging until the original right part becomes sorted

# unsorted list of numbers
numbers = [57, 81, 45, 44, 82, 76, 26, 48, 67, 12]
print(f"\nUnsorted numbers: {numbers}\n")

def mergeSort(numbers):

    if len(numbers) > 1: # divides the subparts until it becomes single element
        leftNum = numbers[:len(numbers)//2] # stores first half of the numbers in a variable
        rightNum = numbers[len(numbers)//2:] # stores second half of the numbers in a variable

        # for recursion
        mergeSort(leftNum)
        mergeSort(rightNum)

        leftNumIndex = 0 # keeps tracking of the left most number in the left array
        rightNumIndex = 0 # keeps tracking of the left most number in the right array
        mergedNumIndex = 0 # keeps tracking of the index in the merged array