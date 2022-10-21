#An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

#Your goal is to find that missing element.

def solution(A):
    if(len(A) == 0):
        return 1
    A.sort()

    for i in range(0, len(A)):
        if A[i] != i+1:
            return i+1
    return (len(A) + 1)
    
    pass