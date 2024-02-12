#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.strip().lower()
    if word == "":
        return(False)
    else:
        length = len(word)-1
        wordy = []
        for i in range((length),-1,-1):
            wordy.append(word[i])
        separator = ''
        backwards = separator.join(wordy)
        return(backwards.lower() == word.lower())
        
    
       



if __name__ == '__main__':
    word1 = input()
    print(palindrome(word1))