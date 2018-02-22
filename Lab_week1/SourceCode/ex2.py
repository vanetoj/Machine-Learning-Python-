import math

def sentence():
    words = input("Enter a sentence: ").split()

    if len(words) % 2 == 0:
        middle = words[math.floor(len(words) / 2) - 1 : len(words) // 2 + 1 ]
    else:
        middle = words[len(words) // 2 : len(words) // 2 + 1]
    
    print("Middle words are: [",  ', '.join(middle), ']' )

    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    print("Longest word is " , longest)

    reverse_words = []

    for word in words:
        reverse_words.append( word[::-1] )

    print( "Sentence with reverse words is: " , ' '.join(reverse_words) )

sentence()
