import sys
LI=lambda:list(map(int,sys.stdin.readline().split()))
MI=lambda:map(int,sys.stdin.readline().split())
SI=lambda:sys.stdin.readline().strip('\n')
II=lambda:int(sys.stdin.readline())

t=II()
for j in range(t):
	SI()
	pos=LI()
	val=SI().split()
	ans=[0]*len(pos)
	for i in range(len(pos)):
		ans[pos[i]-1]=val[i]
	print(*ans, sep='\n')
	print(end=('\n' if j<t-1 else ''))
