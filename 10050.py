import sys
LI=lambda:list(map(int,sys.stdin.readline().split()))
MI=lambda:map(int,sys.stdin.readline().split())
SI=lambda:sys.stdin.readline().strip('\n')
II=lambda:int(sys.stdin.readline())

for _ in range(II()):
	n=II()
	h=[0]*(n+1)
	for _ in range(II()):
		v=II()
		for j in range(v,n+1,v):
			if j%7 and j%7!=6:
				h[j]=1
	print(h.count(1))
