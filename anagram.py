# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
s = input()
t = input()
if len(s) != len(t):
    print("False")
    exit()
else:
    freq = {}
for ch in s:
    if ch in freq:
        freq[ch] +=1
    else:
        freq[ch]=1
anagram=True
for ch in t:
    if ch not in freq or freq[ch]==0:
        anagram = False
        break
    freq[ch] -= 1
print(anagram)