# Partition Funtion.
def merge_sort(my_array):
    #  Checking if the array is real.
    if len(my_array) <= 1:
        return my_array

    # Dividing the array in the middle into Left Side and Right Side.
    middle = len(my_array) // 2
    left_side = my_array[:middle]
    right_side = my_array[middle:]

    # Merge Sorted first the Left Side and the Right Side.
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    # Merging the sorted left side and right side.
    return merging(left_side, right_side)


# Main Function.
def merging(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            # i (left) will be increment if it is less than than J (right).
            result.append(left[i])
            i += 1
        else:
            # Else j is increment instead.
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Ask the user to enter the size of the array.
try:
    Sz = int(input("Please enter the array size : "))
except ValueError:
    print("Please enter a valid size for the array.")
    exit()

# Ask the user to enter the values of the array
try:
    array_input = input("Please enter array values separated by spaces : ")
    # Converting the array_output into a list.
    array_output = [int(L) for L in array_input.split()]
except ValueError:
    print("Please enter valid values in the array.")
    exit()

# Checking if the entered length matches with indicated size.
if len(array_output) != Sz:
    print("The number of values entered does not match the size of the array.")
    exit()

# Sorting
sorted_array = merge_sort(array_output)

# Display the Merge sorted array
print("Your Merge Sorted array is:", sorted_array)