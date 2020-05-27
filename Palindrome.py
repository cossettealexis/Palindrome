
while(True):
    word = input("Input String : ")
    reverse = word[len(word)::-1]

    if(word == reverse):
        print("The word " + word + " is a palindrome.")
    else:
        print("The word " + word + " is not a palindrome.")
