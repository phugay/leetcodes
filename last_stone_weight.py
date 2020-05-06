# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

class Solution(object):
    def lastStoneWeight(self, stones):
        sorted_stones = sorted(stones, reverse = True)
        print(sorted_stones)
        i=0
        j=1
        while i<j and j<2:
            sorted_stones = sorted(sorted_stones, reverse = True)
            if (len(sorted_stones)==1):
                print("length 1")
                print(sorted_stones)
                i=j
                return sorted_stones[0]
            elif (len(sorted_stones)==0):
                print("length 0")
                return 0
            elif(len(sorted_stones)==2):
                print("length 2")
                if sorted_stones[0]>sorted_stones[1]:
                    return sorted_stones[0]-sorted_stones[1]
                else:
                    return sorted_stones[1]-sorted_stones[0]
            elif(len(sorted_stones)==3):
                print("length 3")
                sorted_stones = sorted(sorted_stones, reverse = True)
                new_stone = abs(sorted_stones[i] - sorted_stones[j])
                if new_stone >= sorted_stones[j+1]:
                    print("gte",sorted_stones[i],sorted_stones[j])
                    sorted_stones[j] = new_stone 
                    del sorted_stones[i]
                elif new_stone < sorted_stones[j+1]:
                    print("lt",sorted_stones[i],sorted_stones[j])
                    del sorted_stones[i:j+1]
                    sorted_stones.append(new_stone)
                elif new_stone == 0:
                    del sorted_stones[i:j+1]
                    sorted_stones.append(new_stone)
            elif sorted_stones[i]>sorted_stones[j]:
                new_stone = sorted_stones[i] - sorted_stones[j]
                print(new_stone)                
                if new_stone >= sorted_stones[j+1]:
                    print("gte",sorted_stones[i],sorted_stones[j])
                    sorted_stones[j] = new_stone 
                    del sorted_stones[i]   
                elif new_stone < sorted_stones[j+1] and new_stone < sorted_stones[j+2]:
                    print("lt and lt",sorted_stones[i],sorted_stones[j])
                    del sorted_stones[i:j+1]
                    sorted_stones.append(new_stone)
                elif new_stone < sorted_stones[j+1] and new_stone >= sorted_stones[j+2]:
                    print("lt and gt",sorted_stones[i],sorted_stones[j])
                    sorted_stones[j] = new_stone 
                    del sorted_stones[i] 
            elif sorted_stones[j]>sorted_stones[i]:
                new_stone = sorted_stones[j] - sorted_stones[i]
                print(new_stone)                
                if new_stone >= sorted_stones[j+1]:
                    print("gte",sorted_stones[i],sorted_stones[j])
                    sorted_stones[j] = new_stone 
                    del sorted_stones[i]    
                elif new_stone < sorted_stones[j+1] and new_stone < sorted_stones[j+2]:
                    print("lte",sorted_stones[i],sorted_stones[j])
                    del sorted_stones[i:j+1]
                    sorted_stones.append(new_stone)
                elif new_stone < sorted_stones[j+1] and new_stone >= sorted_stones[j+2]:
                    print("lt but gt",sorted_stones[i],sorted_stones[j])
                    sorted_stones[j] = new_stone 
                    del sorted_stones[i]    
            elif sorted_stones[i]==sorted_stones[j]:
                del sorted_stones[i:j+1]
            print("----------------")

                
                