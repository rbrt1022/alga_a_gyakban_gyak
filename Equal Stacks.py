#https://www.hackerrank.com/challenges/equal-stacks/problem

def equalStacks(h1, h2, h3):
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    i1, i2, i3 = 0, 0, 0

    while not (sum1 == sum2 == sum3):
        
        max_height = max(sum1, sum2, sum3)

        if sum1 == max_height:
            sum1 -= h1[i1]  
            i1 += 1         
        
        elif sum2 == max_height:
            sum2 -= h2[i2]
            i2 += 1
            
        else:
            sum3 -= h3[i3]
            i3 += 1

    return sum1
