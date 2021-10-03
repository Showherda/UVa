import sys
LI=lambda:list(map(int,sys.stdin.readline().split()))
MI=lambda:map(int,sys.stdin.readline().split())
SI=lambda:sys.stdin.readline().strip('\n')
II=lambda:int(sys.stdin.readline())
sys.setrecursionlimit(100000)
def dfs(p, u):
	global g, tin, low, time, vis, ans
	vis.add(u)
	time+=1
	tin[u]=low[u]=time
	children=0
	try:
		for v in g[u]:
			if v==p:
				continue
			if v in vis:
				low[u]=min(low[u], tin[v])
			else:
				dfs(u, v)
				low[u]=min(low[u], low[v])
				if low[v]>=tin[u] and p!=-1:
					ans.add(u)
				children+=1
		if p==-1 and children>1:
			ans.add(u)
	except:
		pass
cnt=0
while 1:
	cnt+=1
	n=II()
	if not n:
		break
	if cnt!=1:print()
	g={}
	nd=[SI() for i in range(n)]
	for i in range(II()):
		u, v=SI().split()
		try:
			g[u].append(v)
		except:
			g[u]=[v]
		try:
			g[v].append(u)
		except:
			g[v]=[u]
	tin, low={}, {}
	time=0
	vis=set()
	ans=set()
	for u in nd:
		if u not in vis:
			dfs(-1, u)
	print(f'City map #{cnt}: {len(ans)} camera(s) found')
	if len(ans):
		print(*sorted(ans), sep='\n')
