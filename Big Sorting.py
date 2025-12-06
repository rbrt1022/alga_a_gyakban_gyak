#https://www.hackerrank.com/challenges/big-sorting/problem

def bigSorting(unsorted):
    buckets = {}
    
    for s in unsorted:
        hossz = len(s)
        if hossz not in buckets:
            buckets[hossz] = []
        buckets[hossz].append(s)
    
    sorted_result = []
    
    for hossz in sorted(buckets.keys()):
        buckets[hossz].sort()
        
        sorted_result.extend(buckets[hossz])
        
    return sorted_result

    
