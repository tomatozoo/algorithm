#타겟 넘버를 만족시키는 subarray num을 찾아라

#모두 positive array

#s = 7, [3,4,2,1,3,2]

#O(n)으로 해결한다면?

#sliding 개념 + 모두 양수임을 활용하면 풀 수 있음

"""포인터 start와 end 모두 0부터 시작하여 누적합이 target s 이상이 될 때까지 end를 증가시켜주면서 진행된다.

만약 누적합이 target s보다 커진 경우에는 start가 가리키는 값을 누적합에서 빼준 뒤 start값을 1 증가시켜줘야 한다.

이를 반복하여 start와 end 사이의 길이가 가장 작은 값을 찾으면 답을 구할 수 있다."""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        sum = nums[0]
        min = len(nums)
        found = False

        if len(nums) == 0: return 0


    # left를 기준으로 판단한다. 

        while start <= end and end < len(nums):
            if sum < target:
                end += 1
                if end < len(nums):
                    sum += nums[end]
            elif sum >= target:
                if min >= (end - start + 1):
                    min = end - start + 1
                    found = True
                if sum > target:
                    
                    sum -= nums[(start)]
                    start += 1

                else:
                    end += 1
                    if end < len(nums):
                        sum += nums[end]
        if found==True:
            return min
        return 0


    # 만약에 누적합이 target보다 커지면 길이를 저장하고, left를 옮긴다. 


    # 그렇게 left >= right가 되면, return 0

#hi