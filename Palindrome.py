
choice="Y"
while choice.upper()=="Y":
    word = input("Input String : ")
    reverse = word[len(word)::-1]
    if (word == reverse):
        print("The word " + word + " is a palindrome.")
    else:
        print("The word " + word + " is not a palindrome.")
    choice=input("Do you wish to check for more words, if YES press 'Y' else press anything else")
