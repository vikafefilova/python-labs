"""# 1
a=int(input('a '))
b=int(input('b '))
c=int(input('c '))
if a==b==c:
    print('все числа равны')
elif a==b:
    if a>c:
        print('max ', a, b)
        print('min ', c)
    else:
        print('max ', c)
        print('min ', a, b)
elif a==c:
    if a>b:
        print('max ', a, c)
        print('min ', b)
    else:
        print('max ', b)
        print('min ', a, c)
elif c==b:
    if c>a:
        print('max ', c, b)
        print('min ', a)
    else:
        print('max ', a)
        print('min ', c, b)
elif a>b and a>c and b>c:
    print('max ', a)
    print('min ', c)
elif a>c and a>b and c>b:
    print('max ', a)
    print('min ', b)
elif b>a and b>c and a>c:
    print('max ', b)
    print('min ', c)
elif b>c and b>a and c>a:
    print('max ', b)
    print('min ', a)
elif c>b and c>a and b>a:
    print('max ', c)
    print('min ', a)
elif c>a and c>b and a>b:
    print('max ', c)
    print('min', b)"""



"""# 2
n=int(input('n '))
e=1
s=''
u=0
for i in range(n):
    s+=str(e)
    e+=1
while u!=n:
    print(s)
    s=s[:-1]
    u+=1"""



'''# 2.2
n=int(input('n '))
e=1
s=''
s1=''
u=0
for i in range(n):
    s+=str(e)
    e+=1
s1=s[1:][::-1] + s
while u!=n:
    print(' '*u, s1)
    s1=s1[1:-1]
    u+=1'''



# 3
n = int(input('n '))
p = []
for i in range(0, n):
    s = [1] * (i + 1)
    for j in range(1, i):
        s[j] = p[i - 1][j - 1] + p[i - 1][j]
    p.append(s)
for r in p:
    print(r)
