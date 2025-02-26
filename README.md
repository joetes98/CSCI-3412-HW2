# CSCI 3412 HW2
## Question 1
###
The results for each function were calculated in python. We solve for n and input the time t into the python function for squareroot, n<sup>2</sup>, n<sup>3</sup>, and 2<sup>n</sup>.

Log(n) is represented as n = 2<sup>t</sup>. Since the results from this function were too large for python to compute.

nLog(n) used the Lambert W function since this equation has no closed form solution for n. The Scipy module has the lambertw function which allows us the find the value of n.

n!: We loop through every value of n until we find the maximum value which satisfies the equation.

## Question 2
###
Executing the insertion sort algoritm and merge sort algorithm on data sets of various sizes demonstrates the power of an efficient algorithm.

The below table shows the exeuction time (in seconds) & the number of comparisons for each algorithm.

**Execution Time**

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Insertion Sort</th>
      <th>Merge Sort</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1000</th>
      <td>0.021</td>
      <td>0.003</td>
    </tr>
    <tr>
      <th>10000</th>
      <td>2.345</td>
      <td>0.039</td>
    </tr>
    <tr>
      <th>100000</th>
      <td>240.403</td>
      <td>0.482</td>
    </tr>
    <tr>
      <th>250000</th>
      <td>1821.183</td>
      <td>1.525</td>
    </tr>
    <tr>
      <th>500000</th>
      <td>8069.402</td>
      <td>3.011</td>
    </tr>
    <tr>
      <th>1000000</th>
      <td>39616.518</td>
      <td>6.714</td>
    </tr>
  </tbody>
</table>


**Number of comparisons**

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Insertion Sort</th>
      <th>Merge Sort</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1000</th>
      <td>246373</td>
      <td>1982</td>
    </tr>
    <tr>
      <th>10000</th>
      <td>224982755</td>
      <td>19979</td>
    </tr>
    <tr>
      <th>100000</th>
      <td>2505219319</td>
      <td>199962</td>
    </tr>
    <tr>
      <th>250000</th>
      <td>15644804958</td>
      <td>499977</td>
    </tr>
    <tr>
      <th>500000</th>
      <td>62475643455</td>
      <td>999983</td>
    </tr>
    <tr>
      <th>1000000</th>
      <td>249925868109</td>
      <td>1999969</td>
    </tr>
  </tbody>
</table>

Both the insertion sort and the merge sort have fast execution times for 1,000 and 10,000 data sizes. When sorting the 100000 data set, the insertion increased by about 4 minutes while the merge sort only increase by about 0.4 seconds. The difference between the two sorting algorithms is even further exemplified as the size of the data sets increase, with the insertion taking up to 11 hours for the 1,000,000 while the merge sort only tool 6.7 seconds.


## Question 3
###
**3.1:** Loop invariant technique means finding a property of alogorithm that is true before each iteration of the algorithm and after each iteration of the alogrithm. If we can prove that both these cases are always true, then the algorithm is correct.

**3.2:** The loop invariant for merge sort is the merged subarrays. Before each iteration, there are two sorted subarrays.  After each iteration, there is a single merged subarray.

**3.3:** For the first iteration, the left and right subarrays have a single element, meaning that these subarrays are sorted.

**3.4:**  When merging the two arrays, we iterate through each array comparing the elements. The smallest available element between the two arrays is selected as the next element in the resulting array. The merged array is then sorted.

**3.5:** The loop terminates after log(n) recursive calls of merge sort. By the maintenance step, we the resulting array is sorted. Therefore, the final array is sorted when the loop terminates.

## Extra Credit
###

Insertion sort has a time complexity of O(n<sup>2</sup>), meaning given a data size of n, the algorithm will complete n<sup>2</sup> total instructions. This is true for both the worst case and the average case. The best case for insertion sort has a time complexity of O(n), this is when the data is already sorted. 

For insertion sort, n<sup>2</sup> is the worst case total instructions. This would occur if the data set is sorted in the opposite order we desire. Therefore it has an upperbound of n<sup>2</sup> instructions/comparison. This can be seen in our data, where the total number of comparison is always less than n<sup>2</sup>.

A similar conclusion can be drawn from the merge sort. Merge sort has a time complexity of O(nlogn), meaning given a data size of n, the algorithm will complete nlogn total instructions. Merge sort however will always have a time complexity of O(nlogn) for the best, average, and worst case. This is due to the fact that we are always dividing our list (logn times) down to n lists, then merging the n list into a single list. The data agrees with the analysis, the total number of comparisons for each data set is less than nlogn

As seen by the data, the execution time of the insertion sort exponentially increases with the the data size. This is due to algorithm having an efficiency of O(n<sup>2</sup>) so the number of comparisons is proportional to the square of the data size.

The merge sort on the other hand has efficiency of O(nlogn), so the execution time has a more linear growth with respect to the data size.

This exercise shows the importantance of choosing the correct algorithm for your task. While an insertion sort may be a good choice if your data is close to sorted or if the data size is small, the algorithm is not fit for dealing with large data sets. Merge sort on the other hand, is able to sort in a matter of seconds, even when dealing with data with millions of elements.