print("Hello there!")

yourSntnc = input("Please Enter your Sentence : \n> ")
print("------------------------------------------")

num_space = 0
num_vowels = 0
num_consonant = 0

for ch_word in yourSntnc:
    if ch_word == ' ':
        num_space = num_space + 1
        
        num_words = num_space + 1