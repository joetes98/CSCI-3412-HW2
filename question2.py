import time
import matplotlib as plt

def insertionSort(A):
    count = 0
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -=1
            count +=1
        A[i+1] = key
    print(f"Number of comparisons: {count}")
    return count

def mergeSort(A):
    global count
    count = 0
    if len(A) > 1:
        # divide
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        mergeSort(left)
        mergeSort(right)
        # merge two halves into sorted list
        i = 0; j = 0; k = 0
        while i < len(left) and j < len(right):
            count += 1
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        # left overs
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
    # print(f"Number of comparisons: {count}")
    return count

def timeEfficiency(funcName, *args, **kwargs):
    # record start time
    startTime = time.time()

    func = funcName(*args)

    # record end time
    endTime = time.time()
    timeEfficiency = endTime - startTime

    print(f"Start time: {startTime}")
    print(f"End Time: {endTime}")
    print(f"Total time: {timeEfficiency}")

    return startTime, endTime, timeEfficiency, func

def main():
    
    fileNames = ["rand1000.txt", "rand10000.txt", "rand100000.txt", 
                 "rand250000.txt", "rand500000.txt", "rand1000000.txt" ]

    print("Select an option\n1. Insertion Sort\n2. Merge Sort")
    userInput = input()

    if int(userInput) == 1:
        
        for name in fileNames:

            with open(name, 'r') as file:
                nums = file.read().split()

                integers = [int(num) for num in nums]
    
            # print(integers)

            start, end, total, count = timeEfficiency(insertionSort, integers)
            # print(integers)

            f = open("insertion_output.txt", 'a')
            f.write(f"File Name: {name}\n")
            f.write(f"Start time: {start}\n")
            f.write(f"End time: {end}\n")
            f.write(f"Total time: {total}\n")
            f.write(f"Number of comparisons: {count}\n\n")
    
    elif int(userInput) == 2:

        for name in fileNames:

            with open(name, 'r') as file:
                nums = file.read().split()

                integers = [int(num) for num in nums]
    
            # print(integers)

            start, end, total, count = timeEfficiency(mergeSort, integers)
            # print(integers)

            f = open("merge_output.txt", 'a')
            f.write(f"File Name: {name}\n")
            f.write(f"Start time: {start}\n")
            f.write(f"End time: {end}\n")
            f.write(f"Total time: {total}\n")
            f.write(f"Number of comparisons: {count}\n\n")

    else:
        print("Not a valid input")

if __name__ == '__main__':
    main()