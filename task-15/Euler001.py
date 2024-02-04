t = int(input())
for x in range(t):
    n = int(input())
    print(sum([i for i in range(n) if i%3==0 or i%5==0]))