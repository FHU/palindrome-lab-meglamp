#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.strip()
    if word == "":
        return(False)
    else:
        length = len(word) -1
        wordy = []
        for i in range((length),0,-1):
            wordy.append(word[i])
        separator = ''
        backwards = separator.join(wordy)
        return(backwards.lower() == word.lower())
    




word1 = input()
print(palindrome(word1))
