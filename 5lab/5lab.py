#1
'''f=open('input.txt').readline()
f2=open('output.txt', 'w+')
p=1
for i in range(0, 19, 2):
    p*=int(f[i])
f2.write(str(p))
f2.close()'''



#2
'''f=open('5lab.2.txt').readlines()
f2=open('5lab.2.2.txt', 'w+')
f.sort()
for i in range(10):
   f2.write(str(f[i]))
f2.close()'''



#3
with open('5lab.3.txt', encoding='utf-8') as file:
    children = []
    for line in file:
        surname, name, age_str = line.strip().split()
        age = int(age_str)
        children.append((surname, name, age))
old = max(children, key=lambda x: x[2])
young = min(children, key=lambda x: x[2])

with open('5lab_old.txt', 'w') as file:
    file.write(f"{old[0]} {old[1]} {old[2]}\n")
with open('5lab_young.txt', 'w') as file:
    file.write(f"{young[0]} {young[1]} {young[2]}\n")