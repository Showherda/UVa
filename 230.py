import sys
LI=lambda:list(map(int,sys.stdin.readline().split()))
MI=lambda:map(int,sys.stdin.readline().split())
SI=lambda:sys.stdin.readline().strip('\n')
II=lambda:int(sys.stdin.readline())
on=[]
tmp=[]
aut={}
while 1:
	b=SI()
	if b[0]=='E':
		break
	t, a=b[1:b.rindex('"')], b[b.rindex('"')+5:]
	on.append(t)
	aut[t]=a
while 1:
	v=SI()
	if v[0]=='E':
		break
	elif v[0]=='S':
		on.sort(key=lambda x:(aut[x],x))
		tmp.sort(key=lambda x:(aut[x],x))
		for t in tmp:
			i=on.index(t)
			if i:
				print(f'Put "{t}" after "{on[i-1]}"')
			else:
				print(f'Put "{t}" first')
		tmp=[]
		print('END')
	else:
		a=v[:v.index(' ')]
		t=v[v.index(' ')+2:-1]
		if a[0]=='B':
			on.remove(t)
		else:
			tmp.append(t)
			on.append(t)
