class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def custom_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def custom_lcm(a, b):
            return abs(a * b) // custom_gcd(a, b)
        
        n = len(nums)
        max_len = 1

        for i in range(n):
            curr_gcd = nums[i]
            curr_lcm = nums[i]
            curr_prod = nums[i]
            
            for j in range(i + 1, n):
                curr_gcd = custom_gcd(curr_gcd, nums[j])
                curr_lcm = custom_lcm(curr_lcm, nums[j])
                curr_prod *= nums[j]
                
                if curr_prod == curr_gcd * curr_lcm:
                    max_len = max(max_len, j - i + 1)
                # Early stop if product grows too big (optional)
                if curr_prod > 1e18:  
                    break

        return max_len