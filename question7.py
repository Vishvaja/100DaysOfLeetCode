class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def isFirstFunc(isFirst):
            bound = -1
            start = 0
            end = len(nums)-1
            
            while(start<=end):
                
                print(start,end)
                mid = (start + end) //2   #Important to put braces to compute properly
                print(nums[mid],target)
                if nums[mid]==target:
                    bound = mid #To know position
                    if(isFirst):
                        end = mid-1
                    else:
                        start = mid+1
                elif(nums[mid]>target):
                    end = mid-1
                else:
                    start = mid+1
            return bound
        lowerBound = isFirstFunc(True)
        upperBound = isFirstFunc(False)
        
        return [lowerBound, upperBound]