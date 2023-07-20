Count frequency of each element in the array Problem statement: Given an array, we have found the number of occurrences of each element in the array.

Examples:

Example 1: Input: arr[] = {10,5,10,15,10,5}; Output: 10 3 5 2 15 1 Explanation: 10 occurs 3 times in the array 5 occurs 2 times in the array 15 occurs 1 time in the array

Example2: Input: arr[] = {2,2,3,4,4,2}; Output: 2 3 3 1 4 2 Explanation: 2 occurs 3 times in the array 3 occurs 1 time in the array 4 occurs 2 time in the array

# approch 1 using 2 loops

a=eval(input())

track=[]

for i in a:

    count=0

    

    for j in a:

        if(i==j):

            count+=1

    if i not in track:

        track.append(i)

        print(i,":",count)        

[10,5,10,15,10,50]
10 : 3
5 : 1
15 : 1
50 : 1

Time Complexity: O(N*N)

Space Complexity: O(N)

#approch 2

a=eval(input())

answer={}

for i in a:

    if(i in answer):

        answer[i]+=1

    else:

        answer[i]=1

print(answer)        

[10,5,10,15,10,50]
{10: 3, 5: 1, 15: 1, 50: 1}

Time Complexity: O(N)

Space Complexity: O(n)
