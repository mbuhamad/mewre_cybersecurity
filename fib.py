# 1,1,2,3,5,8,13,...
# fibonacci series takes place in nature.
# This script calculating fibonacci series to the term n
# Notice how  slow this would make your computer! Do you know why?

def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fib(n-1)+fib(n-2)

print(fib(int(input('Enter to which term you want to calculate fib:'))))