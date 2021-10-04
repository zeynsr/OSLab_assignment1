a=int(input())
b=int(input())
c=int(input())

if(a<b+c)&(b<a+c)&(c<b+a):
    print('possible.')
else :
    print('impossible !')    