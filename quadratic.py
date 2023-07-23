a,b,c=map(int,input().split())#get a input a b c
d=((b**2)-(4*a*c))**0.5 #formula stpes
e=(d-b)/(2*a) #formula steps
f=-(d+b)/(2*a) #formula steps
print(f'{e:.2f}') #print with two decimal value
print(f'{f:.2f}')
