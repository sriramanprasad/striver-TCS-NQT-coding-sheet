Reverse a given Array Problem Statement: You are given an array. The task is to reverse the array and print it.

Examples:

Example 1: Input: N = 5, arr[] = {5,4,3,2,1} Output: {1,2,3,4,5} Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Example 2: Input: N=6 arr[] = {10,20,30,40} Output: {40,30,20,10} Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

#approch 1

a=input()

a=a.split()

l=[]

for i in a[::-1]:

    l.append(int(i))

print(l)    

1 2 3 4
[4, 3, 2, 1]

Time Complexity: O(n), single-pass for reversing array.

Space Complexity: O(n), for the extra array used.

#approch 2

a=eval(input())

p1=0

p2=len(a)-1

while(p1<p2):

    a[p1],a[p2]=a[p2],a[p1]

    p1+=1

    p2-=1

print(a)    

[1, 2,3 ,4]
[4, 3, 2, 1]

Time Complexity: O(n), single-pass involved.

Space Complexity: O(1)
