from Assignment5 import *
import unittest

class testAssignment5(unittest.TestCase):

    def testcreateUnigramDictionary(self):
        self.assertEqual(1,createUnigramDictionary("HP1.txt")["shoo"])
        self.assertEqual(19,createUnigramDictionary("HP1.txt")["harry"])

    def testremoveAllPunctuation(self):
        self.assertEqual(-1, removeAllPunctuation(open("HP1.txt").read(),['.', 'Ms','Mrs','Mr']).find('.'))
        self.assertEqual(-1, removeAllPunctuation(open("HP1.txt").read(),['.', 'Ms','Mrs','Mr']).find('Mr'))

    def testremoveAllNames(self):
        self.assertEqual(-1, removeAllNames(open("HP1.txt").read(),["Harry","Ron","Hermoine"]).find('Harry'))
        self.assertEqual(-1, removeAllNames(open("HP1.txt").read(),["Harry","Ron","Hermoine"]).find('Ron'))

    def testwriteDictToFile(self):
        testDict = {"a":1,"b":2,"c":3}
        writeDictToFile(testDict, "testDictFile.txt")
        f = open("testDictFile.txt")
        string = f.read()
        self.assertNotEqual(-1,string.find("b : 2"))

    def testignoreNames(self):
        g = open("ignoreNamesTest.txt","w")
        g.write("James Jon Joe Harry Jill Julie Jenna")
        ignoreNames("ignoreNamesTest.txt","HPChar.txt")
        f=open("HPMinusNames.txt")
        self.assertEqual(-1, f.read().find("Harry"))
        f=open("HPMinusNames.txt")
        self.assertEqual(-1, f.read().find("harry"))

    def testcreateNameList(self):
        nameList = createNameList("HPChar.txt")
        self.assertEqual(0, nameList.count("Batman"))
        self.assertEqual(1, nameList.count("Snape"))
        self.assertEqual(1, nameList.count("Rons"))

    def testgetSentences(self):
        sentenceList = getSentences("HP1.txt")
        self.assertEqual(0, sentenceList.count("Mr."))
        self.assertEqual(list,type(getSentences("HP1.txt")))

    def testgetBigramFreqFromSentence(self):
        self.assertEqual({"this is":1,"is a":1,"a test":1},getBigramFreqFromSentence("This is a test."))

    def testignoreNamesInSentence(self):
        self.assertEqual(-1, ignoreNamesInSentence(open("HP1.txt").read(),"HPChar.txt").find('Harry'))
        self.assertEqual(-1, ignoreNamesInSentence(open("HP1.txt").read(),"HPChar.txt").find('Ron'))

    def testgetBigramFreqFromFile(self):
        self.assertEqual(5,getBigramFreqFromFile("HP1.txt")["his cloak"])
        self.assertEqual(1,getBigramFreqFromFile("HP1.txt")["cat behavior"])

    def testcreateContingency(self):
        self.assertEqual(list,type(createContingency("abcd defg","bigramFrequencies.txt")))
        self.assertEqual((createUnigramDictionary('HP1.txt')["of"]-2)*2, createContingency("most of","bigramFrequencies.txt")[0][1])

        
    

            
        
        
unittest.main()
