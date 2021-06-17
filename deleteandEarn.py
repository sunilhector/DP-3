# RobberHouseApproch
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if nums is None: return -1
        maxelement = 0
        for element in nums:
            maxelement = max(maxelement, element)
        maxearnarray = [0] * (maxelement + 1)
        print(maxearnarray)

        for element in nums:
            maxearnarray[element] += element
        skip, take = 0, 0
        for maxprofit in maxearnarray:
            temp = skip
            skip = max(skip, take)
            take = temp + maxprofit
        return max(skip, take)

        # SC:- O(n)
    # Time:- O(n)