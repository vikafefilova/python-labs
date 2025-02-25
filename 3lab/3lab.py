#0
n = int(input("введите длину списка "))
l=[]
s=[]
for i in range(n):
    l.append(int(input()))
    if l[i]>l[i-1]:
        s.append(l[i])
print(s)




'''#1
l= [int(i) for i in input().split()] 
n=len(l)
maxx=l[0]
minn = l[0]
for i in range(n):
    if l[i]  > maxx:
        max_i =i
        maxx = l[i]
    elif l[i] < minn:
        min_i =i
        minn = l[i]
l2 = l
l2[max_i] = minn
l2[min_i] = maxx
print(l2)'''





'''#2
t1= [int(i) for i in input().split()]
t2= [int(i) for i in input().split()]
n1=len(t1)
w=0
s=''
for i in range(n1):
    if (t1[i] in t2) and (str(t1[i]) not in s):
        w+=1
        s+=str(t1[i])
print(w)'''





'''# 3
t = [str(i) for i in input().split()]
cl = {}
for i in t:
    if i in cl:
        cl[i] += 1
    else:
        cl[i] = 1
print(*cl.values())'''