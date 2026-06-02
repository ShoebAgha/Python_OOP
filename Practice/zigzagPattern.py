def convert(s: str, numRows: int):
    if numRows==1:
        return s
    
    i=0
    k=1
    g=[[] for _ in range(numRows)]

    for char in s:
        g[i].append(char)
        if i==0:
            k=1
        elif i==numRows-1:
            k=-1
        i+=k
    
    for _ in range(numRows):
        g[_]=''.join(g[_])
    print(g)
    return ''.join(g) 

print(convert("PAYPALISHIRING",numRows=3))       
