#A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

#Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

#The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

#In other words, it is the absolute difference between the sum of the first part and the sum of the second part.


def solution(A):
    if len(A) < 2:
        return 0
    s = sum(A)

    minDiff = 2000
    sL = 0
    for i in range (0, len(A)-1):
        sL +=A[i]
        diff=abs(2*sL- s)
        minDiff = min(minDiff, diff)
    
    return minDiff
