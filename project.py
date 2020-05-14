#Import packages required
import numpy as np
import time

######################  ALGORITHIMS ###################################################
#The below Bubble sort is adapted from the following website:
#https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubble_sort(arr):
    num_in_list = len(arr)
    for i in range(num_in_list):
        for j in range(0, num_in_list-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

#The below Merge sort is adapted from the following website:
#https://www.educative.io/edpresso/merge-sort-in-python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              arr[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1

#The below Counting sort is adapted from the following website:
#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
def count_sort(arr):  
    max_val = max(arr)
    #print(max_val)
    m = max_val + 1
    count = [0] * m                
    
    for a in arr:
    # count occurences
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            arr[i] = a
            i += 1
    return arr

def selection_sort(arr):
    #do something
    arr

def insertion_sort(arr):
    return arr



###################### GENERATE RANDOM DATA ############################################
#generate random int's in array of lenfth number n
def generate_arr(n):
    arr = np.random.randint(0,100,n).tolist()
    return arr

####################### BENCHMARKING ###################################################
bench_values_time = []

def evaluate(func):
    val_n = [100, 250, 500, 750, 1000]
    #val_n = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000]
    for n in val_n:
        arr = generate_arr(n)
        start_time = time.time()
        for i in range(0, 10):
            func(arr)
        finish_time = time.time()
        time_elapsed = finish_time - start_time
        bench_values_time.append([func.__name__, n, time_elapsed/10])
        print(str(n), " Number Size - Time Taken:", str(time_elapsed/10))



######################## MAIN FUNCTION #################################################
def main():
    function_list = [bubble_sort, merge_sort, count_sort]
    for fun in function_list:
        print(fun.__name__)
        evaluate(fun)
    print(bench_values_time)
    

if __name__ == "__main__":
    main()

    