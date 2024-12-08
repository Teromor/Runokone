'''Alkuperäinen ohjelmointi ja englanninkieliset kommentit: Mehrab Jamee :https://gist.github.com/mehrabjamee/5d1d9ae0f589bd577713649dcee30ed7
Generated from Liekki - Runoja by L.Onerva: https://www.gutenberg.org/cache/epub/74689/pg74689.txt
'''
import random
import sys
import time
from urllib.request import urlopen

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./50)

def tervehdysAlkuun():
    slowprint("---L.Onerva might be stirred this time, but never are her words shaken!--")
    print(" ")
    print("Tämä on runokone, joka arpoo sinulle L.Onerva-mixin")
    print(" ")
    print(" ")

print(" ")
tervehdysAlkuun()

def runokone():
    poems = urlopen("https://raw.githubusercontent.com/Teromor/Runokone/main/lonerva_runot.txt").read().decode('utf-8') 
    poems = ''.join([i for i in poems if not i.isdigit()]).replace("\n\n", " ").split(' ')
    # This process the list of poems. Double line breaks separate poems, so they are removed.
    # Splitting along spaces creates a list of all words.
    index = 1
    chain: dict[str, list[str]] = {}
    
    while True:
        try:
            count = int(input("Anna numero 20 ja 200 väliltä:"))
        except ValueError:
            print("En tunnistanyt antamaasi syötettä. Yritä uudestaan ja anna tällä kertaa jokin numero 20-200 välillä kiitos!")
            continue
        if count <= 19 or count > 200:
            print("Anna numero 20:n ja 200:n väliltä")
            continue
        else:
            break

    # This loop creates a dicitonary called "chain". Each key is a word, and the value of each key
    # is an array of the words that immediately followed it.
    print(" ")
    for word in poems[index:]:
        key = poems[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1

    word1 = random.choice(list(chain.keys())) #random first word
    message = word1.capitalize()

    # Picks the next word over and over until word count achieved
    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2

    # creates new file with output and prints it to the terminal
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(message)
    output = open("output.txt","r", encoding="utf-8")
    slowprint(output.read()) 
    print(" ")
    print(" ")
    check = input("Haluatko kokeilla uudestaan? Paina K saadaksesi uuden runon:")
    if check.upper() == "K":
        runokone()
    else:
        print(" ")
        print("Kiitos runokoneen käytöstä!")

runokone()
