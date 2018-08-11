n,k = map(int,input().strip().split(' '))
score = list(map(int,input().strip().split(' ')))
awake = list(map(int,input().strip().split(' ')))
F = [0]*(n+1)
total = 0
for i in range(1,n+1)：
	if awake[i-1] == 1:
		total += score[i-1]
		F[i] = F[i-1]
	else:
		F[i] = F[i-1]+score[i-1]
maxV = 0
for i in range(k,n+1):
	maxV = max(maxV,F[i]-F[i-k])

print(total+maxV)

