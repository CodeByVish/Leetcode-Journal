class Solution:
    def get_sum(self, arr, x):
        
        occr_dict = dict(Counter(arr))
        occr_list = []

        for e, f in occr_dict.items():
            occr_list.append([e, f])

        i = 0
        while(i < len(occr_list) - 1):
            
            j = 0
            while(j < len(occr_list) - 1 - i):
               
                if(occr_list[j][1] < occr_list[j + 1][1]):
                    occr_list[j], occr_list[j + 1] = occr_list[j + 1], occr_list[j]
                
                elif(occr_list[j][1] == occr_list[j + 1][1]):
                    if(occr_list[j][0] < occr_list[j + 1][0]):
                        occr_list[j], occr_list[j + 1] = occr_list[j + 1], occr_list[j]
                
                j += 1            
            i += 1

        _sum = 0
        i = 0
        try:
            while(i < x):
                _sum += occr_list[i][0] * occr_list[i][1]
                i += 1
        except:
            pass
        
        return _sum

    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        
        answer = []

        i = 0
        while(i < len(nums) - k + 1):   
            
            answer.append(self.get_sum(nums[i : i + k], x))
            i += 1

        return answer
        