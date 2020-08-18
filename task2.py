"""
Program: generator.py
Generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random.
"""
import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL",)
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

#adding 2 additional tuples called adjectives and conjunctions to be used 
conjunctions = ("AND","OR","BUT","FOR","SO")
adjectives = ("RED","KIND","FLAT","BLAND","COLD")


#Builds and returns a sentence.
def sentence():
#creating a new variable "conjunctionPhrase" which will only be used in sentence if the  conjunctionRange is more than 50
    conjunctionPhrase = ""
    conjunctionRange = random.randrange(1,101)
    if(conjunctionRange > 50):
        conjunctionPhrase = " " + random.choice(conjunctions) + " " + nounPhrase() + " " + verbPhrase()
    return nounPhrase() + " " + verbPhrase() + conjunctionPhrase

#Builds and returns a noun phrase
def nounPhrase():
#creating a new variable "adjectivePhrase" which will only be used in sentence if the adjectiveRange is more than 40
    adjectivePhrase = ""
    adjectiveRange = random.randrange(1,101)
    if(adjectiveRange > 40):
        adjectivePhrase = " " + random.choice(adjectives)
    return random.choice(articles) + adjectivePhrase +" " + random.choice(nouns)


#Builds and returns a verb phrase.
def verbPhrase():
#creating a new variable "prepositionPhrase" which will only be used in sentence if the prepositionRange is less than 70
    prepositionPhrase = ""
    prepositionRange = random.randrange(0,100)
    if(prepositionRange < 70):
        prepositionPhrase = prepositionalPhrase()
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionPhrase

def prepositionalPhrase():
    #Builds and returns a prepositional phrase.
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    #Allows the user to input the number of sentences to generate.
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
        
if __name__ == "__main__":
    main()