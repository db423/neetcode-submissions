class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lst_of_mx = []
        q = deque()
        l = 0
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]: #Deque property: remove INDICES of values smaller than current indexed value in queue.
                q.pop()
            
            q.append(r)#slide the next index into the deque.
            
            if l > q[0]: #adjust queue to left pointer position
                q.popleft()
            
            if (r+1) >= k: #check if the sublist is the desired range
                lst_of_mx.append(nums[q[0]]) #the deque holds the max at the front.
                l += 1 #adjust the pointer.
        return lst_of_mx