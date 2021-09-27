import sys
LI=lambda:list(map(int,sys.stdin.readline().split()))
MI=lambda:map(int,sys.stdin.readline().split())
SI=lambda:sys.stdin.readline().strip('\n')
II=lambda:int(sys.stdin.readline())

while 1:
	n=II()
	if not n:break
	a=LI()
	a=[a[-1]]+a+[a[0]]
	ans=0
	for i in range(1, n+1):
		ans+=(a[i-1]<a[i] and a[i]>a[i+1]) or (a[i-1]>a[i] and a[i]<a[i+1])
	print(ans)
