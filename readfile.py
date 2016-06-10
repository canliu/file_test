count=0
f=open('test.txt','r')
for line in f:
    count+=1
print(count)
with open('test.txt','r') as f:
    for line in f:
        count+=1
print(count)
