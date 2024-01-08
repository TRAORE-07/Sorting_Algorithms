# The partition function
def my_part(my_array, S, G):
    # The pivot is the middle element in the array.
    DT = my_array[(S + G) // 2]
    while True:
        # S will be incremented every time its value will be lower than DT (the pivot).
        while my_array[S] < DT:
            S += 1

        # G will be decremented every time its value will be greater than DT (the pivot).
        while my_array[G] > DT:
            G -= 1

        # If no crossing between S and G, after the previous loops conditions,
        # S_index and G_index will be swapped.
        if S >= G:
            return G
        my_array[S], my_array[G] = my_array[G], my_array[S]
        S += 1
        G -= 1


# The main function
def quick_sort(my_array, S, G):
    if S < G:
        DT_index = my_part(my_array, S, G)
        quick_sort(my_array, S, DT_index)
        quick_sort(my_array, DT_index + 1, G)

# Ask the user to enter the size of the array.
try:
    Sz = int(input("Please enter the array size : "))
except ValueError:
    print("Please enter a valid size for the array.")
    exit()

# Ask the user to enter the values of the array
try:
    array_input = input("Please enter array values separated by spaces : ")
    array_output = [int(L) for L in array_input.split()]
except ValueError:
    print("Please enter valid values in the array.")
    exit()

# Checking if the entered length matches with indicated size.
if len(array_output) != Sz:
    print("The number of values entered does not match the size of the array.")
    exit()

# Sorting of the array
quick_sort(array_output, 0, len(array_output) - 1)

# Display the quick sorted array
print("Your Quick Sorted array is: ", array_output)
print("Time Complexity is nlogn.")