words = ['bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star','áaa','bbb','çcc','code','doce','deco']
sort_words = {}
for word in words:
    sort_words[word] = ''.join(sorted(word))

def arePermutation(str1, str2): 
    n1 = len(str1) 
    n2 = len(str2)   
    if (n1 != n2): 
        return False  
    a = sorted(str1) 
    str1 = " ".join(a) 
    b = sorted(str2) 
    str2 = " ".join(b)   
    for i in range(0, n1, 1): 
        if (str1[i] != str2[i]): 
            return False 
    return True    
    
anagrams = []
for i in range(len(words)):
    ana = [words[i]]
    for j in range(i + 1, len(words)):
        if sort_words[words[i]] == sort_words[words[j]]:
            ana.append(words[j])
    if len(ana) != 1:
        anagrams.append(ana)


st2 = [item[0] for item in anagrams]
st3 = sorted(st2,reverse = False)
data = []
for i in range(0, len(st3)-1):
    if not arePermutation(st3[i],st3[i+1]):
        data.append(st3[i])
    else:
        data.append(st3[i])

      

