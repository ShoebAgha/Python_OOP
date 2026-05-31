def lengthOfLongestSubstring(s: str):
        currentSubstring=''
        longest=''

        for char in s:
            if len(longest)<len(currentSubstring):
                  longest=currentSubstring
            while char in currentSubstring:
                  currentSubstring=currentSubstring[1:]
            currentSubstring+=char
        if len(longest)<len(currentSubstring):
            longest=currentSubstring
        return len(longest), longest
print(lengthOfLongestSubstring('dvdf'))