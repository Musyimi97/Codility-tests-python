n=[0,1]
def fibonnacci(n):
    if n ==0 or n==1:
        return 0 
    return fibonnacci(n-1) + fibonnacci(n-2)
    
    