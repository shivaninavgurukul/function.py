def check(word):
    ctr=0
    i=0
    while i<len(word):
        if len(word[i])>1 and word[i][0]==word[i][-1]:
            ctr+=1
        i+=1
    return (ctr)
print(check(["abc","123441","mom","shivanis","ABA"]))            
