import sys
LI=lambda:list(map(int,sys.stdin.readline().split()))
MI=lambda:map(int,sys.stdin.readline().split())
SI=lambda:sys.stdin.readline().strip('\n')
II=lambda:int(sys.stdin.readline())

while 1:
	n=II()
	if not n:
		break
	cars=[0]*(n+1)
	ok=1
	for i in range(1,n+1):
		car, pos=MI()
		if abs(pos)>=n or i+pos<1 or i+pos>n or cars[i+pos]:
			ok=0
		else:
			cars[i+pos]=car
	print(*(cars[1:] if ok else [-1]))
