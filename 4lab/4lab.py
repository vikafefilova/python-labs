#1
s={'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
p=input()
for i in s:
    if str(p)==str(i):
        print(s[i])


#2
'''s={'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
p=input()
for i in s:
    if str(p)==str(s[i]):
        print(i)'''


#4
'''p=str(input())
cl=dict()
cl2=dict()
for i in range(len(p)):
    if int(p[i]) not in cl:
        cl[int(p[i])]=1
    else:
        cl[int(p[i])]+=1
cl2=sorted(cl.items(), key=lambda item: item[1], reverse = True)
print(dict(cl2[:3]))'''
