def smallest_element(arr):
    min_val = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    print("The smallest element in the array is:", smallest_element(arr1))
    
    arr2 = [8, 10, 5, 7, 9]
    print("The smallest element in the array is:", smallest_element(arr2))