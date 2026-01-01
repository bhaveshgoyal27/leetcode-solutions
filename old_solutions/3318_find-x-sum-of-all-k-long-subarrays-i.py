# to be optimized by a lot
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
       
        def xsum(nums1, x):
            if len(set(nums1))<=x:
                return sum(nums1)
            counter = {}
            for i in nums1:
                if i in counter:
                    counter[i]+=1
                else:
                    counter[i] = 1
            frequencies = {}
            for i,j in counter.items():
                if j in frequencies:
                    frequencies[j].append(i)
                else:
                    frequencies[j] = [i]
            total = 0
            counts = list(frequencies)
            counts.sort(reverse=True)
            i = 0
            while(x>0):
                a = len(frequencies[counts[i]])
                if a<=x:
                    total += sum(frequencies[counts[i]]*counts[i])
                    x-=a
                else:
                    new = frequencies[counts[i]]
                    new.sort(reverse=True)
                    total += sum(new[:x]*counts[i])
                    x=0
                i+=1
            return total

        n = len(nums)
        result = []
        for i in range(n-k+1):
            result.append(xsum(nums[i: i+k], x))
        return result
