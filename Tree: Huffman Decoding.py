#https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

def decodeHuff(root, s):
    current = root
    
    for char in s:
        
        if char == '0':
            current = current.left  
        else:
            current = current.right 
            
        if current.left is None and current.right is None:
            
            print(current.data, end='')
            
            current = root