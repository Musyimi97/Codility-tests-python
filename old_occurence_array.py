
#A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

#Sort
#Test equality between consecutive elements.
#Increment index by 2.

def solution(A):
    if len(A) ==1:
        return A[0]
    A.sort()
    for i in range(0, len(A)-1, 2):
        if A[i] != A[i+1]:
            return A[i]
    return A[-1]
    pass