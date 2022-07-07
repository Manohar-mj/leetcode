class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        waiting = deque([(1 + delay, 1 + forget, 1)])
        ready = deque()
        total = 0
        ans=1
        MOD = 1000000007
        for i in range(2, n + 1):
            
            while waiting and waiting[0][1] <= i:
                ans -= waiting.popleft()[2]
            while ready and ready[0][1] <= i:
                f = ready.popleft()
                ans -= f[2]
                total -=  f[2]
            while waiting and waiting[0][0] == i:
                f = waiting.popleft()
                ready.append(f)
                total += f[2]
            ans += total
            waiting.append((i + delay, i + forget, total))
