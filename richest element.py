class Solution:
    def majorityElement(self, nums):
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        max=0
        answer=0
        for num in freq:
            if freq[num]>max:
                max=freq[num]
                answer=num
        return answer        
