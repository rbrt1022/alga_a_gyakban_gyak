#https://www.hackerrank.com/challenges/sherlock-and-cost/problem

def cost(B):
    low = 0   
    high = 0
    
    for i in range(1, len(B)):
        prev_low = low
        prev_high = high
        
        low = max(prev_low, prev_high + abs(1 - B[i-1]))
        
        high = max(prev_low + abs(B[i] - 1), prev_high + abs(B[i] - B[i-1]))
        
    return max(low, high)