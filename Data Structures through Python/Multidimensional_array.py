
a=[1,2,3,[4,5,[6,7,8],9],0]
b=a[ : : -1]
# print(b)
c=b[0:len(b):2]
d=c[: : -1]

result = len(b)+len(c)-len(d)

for i in range(len(c)):
    for j in range(len(d)):
        result-=c[i]-d[j]

print(result)        