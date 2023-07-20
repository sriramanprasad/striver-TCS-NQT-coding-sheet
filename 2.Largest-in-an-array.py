#largest number in an array Example 1: Input: arr[] = {2,5,1,3,0}; Output: 5 Explanation: 5 is the largest element in the array.

Example2: Input: arr[] = {8,10,5,7,9}; Output: 10 Explanation: 10 is the largest element in the array.

a=input()

a=a.split()

a.sort()

print(a[len(a)-1])

1 2 3 4
4

Complexity Analysis Time Complexity: O(N*log(N))

Space Complexity: O(1)

#Better approch

a=input()

a=a.split()

maximum=int(a[0])

for i in range(1,len(a)):

    if(int(a[i])>maximum):

        maximum=int(a[i])

print(maximum)        

1 7 6 5
7

Time Complexity: O(N)

Space Complexity: O(1)
