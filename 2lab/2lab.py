#1.
'''r=str(input('Введите r '))
r1=r
l=""
s=1
for i in range(1, len(r)):
 if r[i]==r[i-1]:
  s+=1
 else:
  if s==1:
   l+=r1[0]
   r1=r1[1:]
   s=1
  else:
   l+=r1[0]+str(s)
   r1=r1[s:]
   s=1
 if i==len(r)-1:
  l+=r1[0]+str(s)
print(l)'''





#1.1
'''t = str(input('Введите t '))
p = ''
while t!='':
    if t[1] in '23456789':
        p += t[0] * int(t[1])
        t=t[2:]
    else:
        p += t[0]
        t=t[1:]
print(p)'''





#2.
'''r=str(input('введите строку '))
r1=r
l=''
for i in range(len(r)-1):
    k=1
    for j in range(i+1, len(r)):
        if r1[i]==r1[j] and r1[i]!=" " and r1[j]!=" ":
            k+=1
            r1 = r1[:j] + " " + r1[j+1:]
    l+=str(k)
e=1
while e<=3:
    m=0
    im=0
    for i in range(len(l)):
        if int(l[i]) > m:
            m=int(l[i])
            im=i
    print(r[im], l[im])
    l = l.replace(l[im], '0', 1)
    e+=1'''




#3
l1= ["ноль", 'один', "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
l2= ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
l3= ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
l4= ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
p=int(input('введите число '))
if p<=9:
    print(l1[p])
elif p>=10 and p<=19:
    print(l2[int(str(p)[1])])
elif p==20 or p==30 or p==40 or p==50 or p==60 or p==70 or p==80 or p==90:
    print(l3[int(str(p)[0])-2])
elif p>=20 and p<=99:
    print(l3[int(str(p)[0])-2], l1[int(str(p)[1])])
elif p==100 or p==200 or p==300 or p==400 or p==500 or p==600 or p==700 or p==800 or p==900:
    print(l4[int(str(p)[0])-1])
elif p>=100 and p<=999:
    if str(p)[2]=='0':
        print(l4[int(str(p)[0])-1], l3[int(str(p)[1])-2])
    else:
        print(l4[int(str(p)[0])-1], l3[int(str(p)[1])-2], l1[int(str(p)[2])])