import random

# function to accept the filename as parameter
def readFile(filename):
    
    #Opening the file and saving the file object in a variable
    openFile = open(filename)
    
    #Now using the readlines() function to read all lines from file object and convert file object into a list
    wordList = openFile.readlines()
    listOfWords = [] # creating new array
    
    #using for loop to access list items and saving in array and converting array to a Tuple
    for word in wordList:
        word = word.strip()
        listOfWords.append(word)
    makeTuple = tuple(listOfWords)
    return makeTuple

#accessing different files using readfile() function and saving as touple in different variables
nouns = readFile("noun.txt")
articles = readFile("articles.txt")
prepositions = readFile("prepositions.txt")
verbs = readFile("verbs.txt")


def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase() 

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
        
if __name__ == "__main__":
    main()
