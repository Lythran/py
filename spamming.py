#This will ask the user to spam a certain word or words by however many times they want
def spamming():
    ask_spam = input("What word would you like me to spam?: ")
    amount = int(input("How many times would you like me to say it?: "))
    print(amount * ask_spam)
spamming()