import time

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
        f.write(f"Total time: {total}\n\n")
        f.write(f"Number of comparisons: {count}")

    
if __name__ == '__main__':
    main()