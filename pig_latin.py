import string


def pig_latin(s: str)-> str:
        
    """
    This function is based on a child's game, where words are transformed 
    into Piglatin.
    Words beginning with vowels have `way` added to the end of them.
    Words that begin with consonants, have all the consonants before 
    the first vowel removed then are concatenated at the
    end of the word, followed by an `ay`
    words that are made up of all consonants are treated similary like the
    previous rule an "ay" added to the end of them.
    PUNCTUATIONS and CAPITALIZATION ARE RETAINED
    
    Arguments: s - A string of words
    Returns: A string of transformed words
    """
    #Line 90 turns the sentence into a list of strings "s"
    s = s.split(" ")

    #new_string variable to store a list of transformed strings
    new_string = []

    #vowels, a string of vowels 'aeiou'
    vowels = "aeiou"

    #this is the main for loop described earlier in the introductory part
    for word in s:
        r_word = word[::-1] #this reversed word is used for punctuation test
        capitalize = False #used for capitalization test
        punctuated = False #used for punctuation position test
        consonants = True  #used for vowel position test

        #if statement from Lines 105 - 106 refer to zeroth test in intro
        if word[0].isupper(): #checks if the first letter of a word is upper
            capitalize = True #True if word is capitalized
        word = word.casefold() #turns the letters of the word 
                            # to lowercase for ease

        #for loop for the punctuation test explained in the introductory part
        #of the source code
        for j in range(0, len(word)):
            punctuated = punctuated or (r_word[j] not in string.punctuation)
            if punctuated ==  True:
                p = len(word) - j #helps to determine punctuation position
                break
        
        #for loop for the vowel position test described 
        #in the introduction part of the source code
        for k in range(0, len(word)):
            consonants = consonants and (word[k].casefold() not in vowels)
            if consonants == False:    
                c = k - 1 #helps to determine first vowel position
                break
        
        #if else blocks described in the inductory part of the source code
        #to transform the word based on the results of the three tests
        #zeroth test, first test then second test

        #if the words starts with a vowel c equals -1
        if not consonants and c == -1:
            new_word = word[:p] + "way" + word[p:] #`way` added accordingly

        
        #else if there are consonat(s) to start and a vowel in the word
        elif not consonants:
            new_word = word[c+1:p] + word[:c+1] + "ay" + word[p:] #`ay` added

        #else: meaning the word is made up of all consonants
        else:
            new_word = word[:p] + "ay" + word[p:] #`ay` added, no vowels

        #capitalizes the word if the input word was indeed capitalized.
        if capitalize:   #if True
            new_word = new_word.capitalize() #capitalized word
        
        #append the transformed word to a list of strings `new_string`
        new_string.append(new_word)
    
    #creates a string from the list of transformed words/strings
    new_string =  " ".join(new_string)

    #returns the transformed string, congratulations
    return new_string

