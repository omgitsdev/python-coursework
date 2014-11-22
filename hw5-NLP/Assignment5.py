badChar = ['.','!','&',',','?',':','-','"','(',')','[',']','\r',';','Ms','Mrs','Mr']   ## find way to avoid global variable
def createUnigramDictionary(fileName):
    hpDict = {}
    f = open(fileName)
    string = f.read().lower()
    string = removeAllPunctuation(string, badChar)          # figure out way to avoid repeat calls
    wordList = string.split()
    for word in wordList:
        hpDict[word] = wordList.count(word)                 #make function to create dictionary, reuse in bigram
    return hpDict


def removeAllPunctuation(string, disallowedCharachters):
    for i in range(len(disallowedCharachters)):
        string = string.replace(disallowedCharachters[i],' ')
    string = string.replace('\'','')
    return string

def removeAllNames(string, names):
    textList = string.split()
    for i in range(0,len(textList)):
        for j in range(0,len(names)):
            if (textList[i].find(names[j]) >= 0):
                textList[i] = "#"


    output = " ".join(textList)
    return output

def writeDictToFile(dictionary,filename):
    f = open(filename,"w")
    keyList = dictionary.keys()
    valueList = dictionary.values()
    for i in range(0,len(keyList)):
        f.write(keyList[i])
        f.write(" : ")
        f.write(str(valueList[i]))
        f.write("\n")

def ignoreNames(mainfilename, charachterfilename):      ## choose better variable names
    g = open(mainfilename)
    string = g.read()
    f = open(charachterfilename)
    nameList = createNameList(charachterfilename)
    string1 = removeAllPunctuation(string, badChar) 
    string2 = removeAllNames(string1, nameList)
    h = open("HPMinusNames.txt","w")
    h.write(string2)
    
def createNameList(filename):
    f = open(filename)
    nameList = []
    line = f.readline()
    while line:
        nameList.extend(line.split())
        for i in range(0,len(line.split())):
            nameList.append(line.split()[i] + "s")
        line = f.readline()
    return nameList

def getSentences(fileName):
    f = open(fileName)
    string = f.read()
    string1 = removeAllPunctuation(string, ["Ms.","Mrs.","Mr.",".."])
    sentenceList = string1.split(".")    
    return sentenceList
    
def getBigramFreqFromSentence(sentence):
    cleanSentence =(removeAllPunctuation(sentence, badChar))
    cleanSentence = ignoreNamesInSentence(cleanSentence,"HPChar.txt").lower().replace("#",'')
    sentenceList = cleanSentence.split()
    bigramList = []
    for i in range(0, len(sentenceList)-1):
        bigramList.append(sentenceList[i] + " " + sentenceList[i+1])
    bigramDict = {}
    for bigram in bigramList:
        bigramDict[bigram] = bigramList.count(bigram)
    return bigramDict
    
def ignoreNamesInSentence(string, charachterfilename):
    outputString = removeAllNames(string,createNameList(charachterfilename))
    return outputString

def getBigramFreqFromFile(filename):
    sentenceList = getSentences(filename)
    bigramDict = {}
    for i in range(0,len(sentenceList)-1):
        tempDict = getBigramFreqFromSentence(sentenceList[i])
        for j in range(0,len(tempDict)):
            tempKey, tempVal = tempDict.popitem()
            if bigramDict.has_key(tempKey):
                bigramDict[tempKey] += tempVal
            else:
                bigramDict[tempKey] = tempVal
                
    return bigramDict

def createContingency(bigram, bigramfilename):
    bigramList = bigram.split()
    word1 = 0
    word2 = 0
    together = 0
    neither = 0
    f = open(bigramfilename)
    line = f.readline().split()
    while line:
        if ((line[0] == bigramList[0]) and (line[1] == bigramList[1])):
            together += int(line[3])
        elif (line[0] == bigramList[0]) or (line[1]== bigramList[0]):
            word1 += int(line[3])
        elif (line[0] == bigramList[1]) or (line[1]== bigramList[1]):
            word2 += int(line[3])
        else:
            neither += 1
        line = f.readline().split()
    return [[together, word2],[word1,neither]]
             
    
def main():
    readText = "HP1.txt"
    writeText = "unigramFrequencies.txt"
    charachterfilename = "HPChar.txt"
    dictionary = createUnigramDictionary(readText)
    ignoreNames(readText,charachterfilename)
    dictionary2 = createUnigramDictionary("HPMinusNames.txt")
    writeDictToFile(dictionary, writeText)
    writeDictToFile(dictionary2, "unigramFrequenciesMinusNames.txt")
    bigramDict = getBigramFreqFromFile(readText)
    writeDictToFile(bigramDict, "bigramFrequencies.txt")
    matrix = createContingency("most of","bigramFrequencies.txt")
    print matrix

    
