# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0

    for i in range(elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]

            b += 1

        elif b >= len(arrB):
            merged_arr[i] = arrA[a]

            a += 1

        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]

            a += 1
        
        else:
            merged_arr[i] = arrB[b]

            b += 1
    return merged_arr



    


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right) 
    
    


   

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    left_array = arr[start:mid + 1]
    right_array = arr[mid + 1: end + 1]

    left_index = 0
    right_index = 0
    sorted_index = start

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            arr[sorted_index] = left_array[left_index]
            left_index += 1

        else:
            arr[sorted_index] = right_array[right_index]
            right_index += 1

        sorted_index += 1

    while left_index < len(left_array):
        arr[sorted_index] = left_array[left_index]
        left_index += 1
        sorted_index += 1

    while right_index < len(right_array):
        arr[sorted_index] = right_array[right_index]
        right_index += 1
        sorted_index += 1




    return arr


def merge_sort_in_place(arr, left, right):
    # Your code here

    if left >= right:
        return arr

    mid = (left + right) // 2
    merge_sort_in_place(arr, left, mid)
    merge_sort_in_place(arr, mid + 1, right)
    merge_in_place(arr, left, mid, right)
    
    



    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
