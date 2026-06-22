class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lst_of_mx = []
        q = deque()
        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]: #Deque property: remove values smaller than current indexed value in queue.
                q.pop()
            
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if (r+1) >= k:
                lst_of_mx.append(nums[q[0]])
                l += 1
        return lst_of_mx