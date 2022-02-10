li=[int(t) for t in input().split(',')]
j=1
di=dict()
while j<=9:
	 c=0
	 for i in li:
	 	if i%j==0:
	 		c=c+1
	 di[j]=c
	 j=j+1
print(di)
