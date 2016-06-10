count=0
f=open('test','r')
for line in f:
    count+=1
print(count)
with open('test','r') as f:
    for line in f:
        count+=1
print(count)
