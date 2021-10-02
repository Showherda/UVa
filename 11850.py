import sys
LI=lambda:list(map(int,sys.stdin.readline().split()))
MI=lambda:map(int,sys.stdin.readline().split())
SI=lambda:sys.stdin.readline().strip('\n')
II=lambda:int(sys.stdin.readline())

while 1:
	n=II()
	if not n:break
	s=sorted(II() for i in range(n))
	ok=1
	p=0
	for v in s:
		if v<=p:
			p=v+200
		else:
			ok=0
	if p<1422:ok=0
	p=s[-1]+200-1422
	if p<0:ok=0
	p=1422-p
	for v in s[::-1]:
		if v>=p:
			p=v-200
		else:
			ok=0
	if p>0:ok=0
	print(('' if ok else 'IM')+'POSSIBLE')
