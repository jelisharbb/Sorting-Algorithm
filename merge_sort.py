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

        # merging
        while leftNumIndex < len(leftNum) and rightNumIndex < len(rightNum): # compares the leftmost number of the left subarray with the left most number in the right subarray

            if leftNum[leftNumIndex] < rightNum[rightNumIndex]: # if the leftmost number in the left subarray is smaller, it will be stored in a new variable
                numbers[mergedNumIndex] = leftNum[leftNumIndex]
                leftNumIndex += 1
            
            else: # if the leftmost number in the right subarray is smaller, it will be stored in a new variable
                numbers[mergedNumIndex] = rightNum[rightNumIndex]
                rightNumIndex += 1

            mergedNumIndex += 1
        
        # merging the left over numbers of the left subarray
        while leftNumIndex < len(leftNum):
            numbers[mergedNumIndex] = leftNum[leftNumIndex]
            leftNumIndex += 1
            mergedNumIndex += 1

        # merging the left over numbers of the right subarray
        while rightNumIndex < len(rightNum):
            numbers[mergedNumIndex] = rightNum[rightNumIndex]
            rightNumIndex += 1
            mergedNumIndex +=1