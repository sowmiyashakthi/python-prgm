def findSum(N,K):
    ans = 0;
    for i in range(1, N + 1):
        ans += (i % K(;
    return ans;
N = 10;
K =2;
print(findSum(N, K));
