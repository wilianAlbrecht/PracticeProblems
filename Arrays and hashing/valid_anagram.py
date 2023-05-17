"""
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

def validator(s, l):
    match_position = []
    i = 0
    while i < len(s):
        equal_letter = False
        x = 0 
        while x < len(l):
            ## validates if the letters are same
            if s[i] == l[x]:
                equal_letter = True
                ## validates if not is the first letter
                if i != 0:
                    repeat = False
                    ## validates if the letter has already been found before, to differentiate the repeated letters in the word
                    for match in match_position:
                        if match == x:
                            repeat = True
                            equal_letter = False
                    
                    if repeat == False:
                        match_position.append(x)
                        break

                else:
                    match_position.append(x)
                    break
            x += 1
        ## if the letter are not same return false
        if equal_letter == False:
            return False
        
        i += 1
    
    return True


s = input("Fist word ")
l = input("Second word ")

## validates if the words have the same number of letters
if len(s) == len(l):
    ## case True, validates if the words are anagrams
    result = validator(s, l)

    if result == False:
        print("The words are not anagrams")
    else:
        print("The words are anagrams")
else:
    ## case False, send a error message
    print("Error. The words must have the same number of letters.")

