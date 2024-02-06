#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    if word == "":
        return(False)
    else:
        word = word.strip()
        length = len(word)
        wordy = []
        for i in range((length),0,-1):
            wordy.append(word[i-1])
        separator = ''
        backwards = separator.join(wordy)
        return(backwards.lower() == word.lower())



word1 = input()
print(palindrome(word1))
