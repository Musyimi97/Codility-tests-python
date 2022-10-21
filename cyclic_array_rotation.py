#An array A consisting of N integers is given.
#Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place.


def solution(A,K):
    N =len(A)
    B = [None] * N
    for i in range (0, N):
        B[(i+K) %N] = A[i]
    return B
    pass
    