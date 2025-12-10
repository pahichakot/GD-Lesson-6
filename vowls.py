vowels = ("a", "e", "i", "o", "u")

#Input from user
choice = input("Please enter a word : ")

for i in choice:
    if i in vowels:
        print(i)