def isMatch(s: str, p: str):
    if p=='*':
        return True
    s_i=0
    p_i=0
    match=''
    s_len=len(s)
    p_len=len(p)

    while p_i<p_len and s_i<s_len:
        if p[p_i]=='.':
            match+=s[s_i]
            s_i+=1
            p_i+=1
        elif p[p_i]=='*':
            match+=match[-1]*(s_len-s_i-1)
            p_i+=1
            break
        elif s[s_i]==p[p_i]:
            match+=s[s_i]
            s_i+=1
            p_i+=1
        else:
            return False
    

    while p_i<p_len:
        if p[p_i]!='*':
            return False
        else:
            p_i+=1
    
    for i in range(len(match)):
        if match[i]!=s[i]:
            return False
    if len(match)==s_len:
        return True

    # while s_i<s_len:
    #     if p[p_i]=='.':
    #         s_i+=1
    #         p_i+=1
    #     elif p[p_i]=='*':
    #         s_i+=1
    #     elif s[s_i]==p[p_i]:
    #         s_i+=1
    #         p_i+=1
    #     else:
    #         return False
    
    # while p_i<p_len:
    #     if p[p_i]!='*':
    #         return False
    #     return True

print(isMatch(s='aa',p='a'))

    