#!/usr/bin/env python3

# Define bubble sort function
def bubble_sort(elements):

    # Outer loop to repeatedly float the largest element to the end
    for j in range(len(elements)-1):
        # Define boolean to track when elements are no longer being sorted
        sorted = True
        # Inner loop to float the largest element to the end
        # Subtract iterator of outer loop (j) to prevent comapring already sorted elements
        for i in range(len(elements)-1-j):
            # Check if current element is greater than the next element
            if elements[i] > elements[i+1]:
                # Set the current element to a temporary variable
                tmp = elements[i]
                # Set the current element to the elements of the next element
                elements[i] = elements[i+1]
                # Set the next element to the original elements of the first element
                elements[i+1] = tmp
                # Set sorted to False if sorting is still happening
                sorted = False
        # If sorting hasn't happened then sorting is complete
        if sorted:
            break

if __name__ == "__main__":

    # Unsorted array/list of elements to test with
    elements = [23,12,17,35,34,48,10,42,6,25]

    # Sorted array/list of elements to test with
    # elements = [6,10,12,17,23,25,34,35,42,48]

    # Unsorted array/list of string elements to test with
    # elements = ["banana","blueberry","orange","apple","grape","pear"]

    # Print initial array/list1
    print("\nInitial list: " + str(elements))

    # Run elements through bubble sort function
    bubble_sort(elements)

    # Print elements after bubble sorting
    print("\nSorted list: " + str(elements))