print("Hello there!")

yourSntnc = input("Please Enter your Sentence : \n> ")
print("------------------------------------------")

num_space = 0
num_vowels = 0
num_consonant = 0

#number of words
for ch_word in yourSntnc:
    if ch_word == ' ':
        num_space = num_space + 1
        
        num_words = num_space + 1

#number of vowels and consonants
for letter in range(0, len(yourSntnc)):
         
    input_letters = yourSntnc[letter]
 
    if ( (input_letters >= 'a' and input_letters <= 'z') or (input_letters >= 'A' and input_letters <= 'Z') ):
   
        input_letters = input_letters.lower()
 
        if (input_letters == 'a' or input_letters == 'e' or input_letters == 'i' or input_letters == 'o' or input_letters == 'u'):
                num_vowels += 1
        else:
                num_consonant += 1

print("------------------------------------------")
print("Input:", yourSntnc)
print("Words:", num_words)
print("Vowels:", num_vowels)
print("Consonant:", num_consonant)