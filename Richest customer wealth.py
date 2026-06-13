class Solution:
    def maximumWealth(self, accounts):
        richest=0
        for amount in accounts:
            wealth=sum(amount)
            if wealth>richest:
                richest=wealth
        return(richest)
        
