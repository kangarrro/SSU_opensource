# SSU 1-2 Discrete Math Assignment
import random
import time


def selection_sort(input_arr):
    for i in range(len(input_arr)-1, -1, -1):
        max_index = i
        for j in range(i-1, -1, -1):
            if input_arr[max_index] < input_arr[j]:
                max_index = j

        input_arr[i], input_arr[max_index] = input_arr[max_index], input_arr[i]
    return input_arr


def bubble_sort(input_arr):
    n = len(input_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if input_arr[j] > input_arr[j+1]:
                input_arr[j+1], input_arr[j] = input_arr[j], input_arr[j+1]
    return input_arr


def insertion_sort(input_arr):
    for i in range(1, len(input_arr)):
        key = input_arr[i]

        j = i-1
        while j >= 0 and key < input_arr[j]:
            input_arr[j+1] = input_arr[j]
            j -= 1
        input_arr[j+1] = key
    return input_arr


test_data = [i for i in range(10000)]

# data섞은 후, Bubble Sort 시간측정  -  Lab 1-1
random.shuffle(test_data)
time_before = time.time()
selection_sort(test_data)
time_after = time.time()

selection_sort_time = time_after - time_before


# data섞은 후, Bubble Sort 시간측정  -  Lab 1-2
random.shuffle(test_data)
time_before = time.time()
bubble_sort(test_data)
time_after = time.time()

bubble_sort_time = time_after - time_before


# data섞은 후, Bubble Sort 시간측정  -  Lab 1-3
random.shuffle(test_data)
time_before = time.time()
insertion_sort(test_data)
time_after = time.time()

insertion_sort_time = time_after - time_before

# data섞은 후, Python 기본 Sort 시간측정  -  Lab 1-7
random.shuffle(test_data)
time_before = time.time()
test_data.sort()
time_after = time.time()

python_sort_time = time_after - time_before

print(f"selection_sort : {selection_sort_time}\nbubble_sort    : {bubble_sort_time}\ninsertion_sort : {insertion_sort_time}\npython_sort    : {python_sort_time}")
# 출력 결과 :
#   selection_sort : 5.589369058609009
#   bubble_sort    : 11.584749937057495
#   insertion_sort : 5.313746929168701
#   python_sort    : 0.0011792182922363281
