#!/bin/python3
# Reverse the given array
# Two lists are provided, the first contains the number of elements in the second list.
# Reverse the second list

class reverseArray:

    def __init__(self, arr_count, arr):
        self.arr_count = int(arr_count.strip())
        self.arr = list(map(int, arr.rstrip().split()))
        self.new_arr = []

    def reverseArray(self):
        # Write your code here

        for i in range(self.arr_count):

            self.new_arr.append(self.arr[self.arr_count - i - 1])

        return print(self.new_arr)
