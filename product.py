# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=product(a,b)
print(*c)