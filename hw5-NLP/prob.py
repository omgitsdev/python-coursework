from Assignment5 import *

def probStart(startString, filename):
    outputFile = 'commonStartingWords.txt'
    f = open(filename)
    splittableString = removeAllPunctuation(f.read(),["Ms.","Mrs.","Mr.",".."])
    sentenceList = splittableString.split('.')
    cleanSentenceList = [removeAllPunctuation(sentenceList[x], badChar) for x in range(0,len(sentenceList))]
    firstWord = map(lambda x : x.split()[0].lower(),cleanSentenceList)
    numWords = float(len(firstWord))
    f.close()
    f = open(outputFile,'w')
    f.write(' '.join(firstWord))
    f.close()
    firstWordDict = createUnigramDictionary(outputFile)
    keyList = firstWordDict.keys()
    for i in range(0,len(keyList)):
        firstWordDict[keyList[i]] = firstWordDict[keyList[i]]/numWords 
    writeDictToFile(firstWordDict,outputFile)
    return firstWordDict[startString]

def probSentence(sentence):
    sentenceList = sentence.split()
    prob = probStart(sentenceList[0],"HP1.txt")
    for i in range(1,len(sentenceList)):
        nextItem = sentenceList[i-1] + ' ' + sentenceList[i]
        contingencyMatrix = createContingency(nextItem, "bigramFrequencies.txt")
        prob *= (float(contingencyMatrix[0][0])/(float(contingencyMatrix[0][0]) + float(contingencyMatrix[1][1])))      
    return prob

def maxProb():
    f = open("bigramFrequencies.txt")
    topTell = f.tell()
    lines = f.readlines()
    f.seek(topTell)
    firstWord, secondWord, bigramFreq = [],[],[]
    for i in range(0,len(lines)):
        line = f.readline().split()
        firstWord.append(line[0])
        secondWord.append(line[1])
        bigramFreq.append(int(line[3]))

    f.close()
    bigramNum = float(sum(bigramFreq))
    bigramLen = range(0,len(firstWord))
    f = open("commonStartingWords.txt")
    topTell = f.tell()
    lines = f.readlines()
    f.seek(topTell)
    initialWord, initialProb = [],[]
    for i in range(0,len(lines)):
        line = f.readline().split()
        initialWord.append(line[0])
        initialProb.append(float(line[2]))
    f.close()
    probTracker = float(0)
    tempProb = float()
    bigramTracker = []
    
    #Probably a way to do this with recursion... this works for now
    for i in range(0,len(initialWord)): #word1
        for j in bigramLen:
            if initialWord[i] == secondWord[j]:  #word2
                for k in bigramLen:
                    if firstWord[k] == secondWord[j]:   #word3
                        for l in bigramLen:
                            if firstWord[l] == secondWord[k]:   #word4, word5
                                tempProb = initialProb[i]*(bigramFreq[j]/bigramNum)*(bigramFreq[k]/bigramNum)*(bigramFreq[l]/bigramNum)
                                if tempProb > probTracker:
                                    print 'ding!'
                                    probTracker = tempProb
                                    bigramTracker = [i,j,k,l]
    print bigramTracker
    print initialWord[bigramTracker[0]] +' '+firstWord[bigramTracker[1]]+' '+firstWord[bigramTracker[2]]+' '+firstWord[bigramTracker[3]]+' '+secondWord[bigramTracker[3]]
