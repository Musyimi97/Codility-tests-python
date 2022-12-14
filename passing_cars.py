#A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

#Array A contains only 0s and/or 1s:

#0 represents a car traveling east,
#1 represents a car traveling west.
#The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
#
#For example, consider array A such that:
#
#  A[0] = 0
#  A[1] = 1
#  A[2] = 0
#  A[3] = 1
#  A[4] = 1
#We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
#
#Write a function:
#
#def solution(A)


#that, given a non-empty array A of N integers, returns the number of pairs of passing cars.
#
#The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

def solution(A):
    sE=0
    s=0 
    for i in range(0, len(A)):
        if A[i]==0:
            sE+=1
        elif A[i]==1:
            s+sE
    if s>1000000000:
        return -1
    else:
        return s
    pass
            