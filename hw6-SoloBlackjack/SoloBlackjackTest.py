#Jingru Zhu and Dev Sethi
#CIT 590, Fall 2013

from SoloBlackjack import *
from cards import*
import unittest
class testSoloBlackjack(unittest.TestCase):
    """ setUp the method for default status"""
    def setUp(self):
        table = {1:Card(10,'D'),2:Card(7,'H'),3:Card(2,'D'),4:Card(6,'S'), 5:Card(10,'H'),
                 6:Card(10,'C'),7:Card(9,'S'),8:Card(10,'H'),9:Card(4,'C'),10:Card(10,'D'),
                 11:Card(10,'S'),12:Card(5, 'S'),13:Card(6,'C'),
                 14:Card(4,'S'),15:Card(10,'S'),16:Card(5,'C')}
        return table
        '''table2 = {1:Card('K','D'),2:Card(7,'H'),3:Card(2,'D'),4:Card(6,'S'), 5:Card('J','H'),
                 6:Card('J','C'),7:Card(9,'S'),8:Card('Q','H'),9:Card(4,'C'),10:Card(10,'D'),
                 11:Card(10,'S'),12:Card(5, 'S'),13:Card(6,'C'),
                 14:Card(4,'S'),15:Card('K','S'),16:Card(5,'C')}
        '''
        
    def testrowScore(self):
        '''assures that scores of individual rows are correct'''
        b = BlackJack()
        b.space = self.setUp()
        for i in range(1,len(b.space)+1):
            b.space[i] = b.space[i].get_rank()
        self.assertEqual(4,b.rowScore(4))
        b.space[14] = 6         #modifies on of the values to test a different score
        self.assertEqual(7,b.rowScore(4))

    def testcolScore(self):
        '''assures that scores of individual columns are correct'''
        b = BlackJack()
        b.space = self.setUp()
        for i in range(1,len(b.space)+1):
            b.space[i] = b.space[i].get_rank()
        self.assertEqual(5,b.colScore(1))
        
    def testscoreGame(self):
        '''Assures complete score calculates correctly, incorporates rowScore and colScore'''
        b = BlackJack()
        b.space = self.setUp()
        for i in range(1,len(b.space)+1):
            b.space[i] = b.space[i].get_rank()
        self.assertEqual(28,b.scoreGame())
       
    def testaceCalc(self):
        '''Tests conversion of face cards to value of 10
        Tests that Ace defaults to 11 and two-Card columns allow 10-point blackjack'''
        b = BlackJack()
        b.space = self.setUp()
        """Change the table to have J,Q,K and A before calculation"""
        b.space[1] = Card('A','D')
        b.space[5] = Card('J','H')
        b.space[6] = Card('J','C')
        b.space[8] = Card('Q','H')
        b.space[15]= Card('K','S')
        self.assertEqual(33,b.aceCalc())
        b.space = self.setUp()
        b.space[1] = Card('K','D')
        self.assertEqual(28,b.aceCalc())
        
      
        
    #def testplaceCard(self):
        #Simply assigns value to a dictionary key, no test needed
    #def testtrashCard(self):
        #Simply assigns value to a dictionary key, no test needed
        
    def testisFull(self):
        '''Tests that function returns correct bool when space is occupied by
        a non-int'''
        b = BlackJack()
        b.space = self.setUp()
        self.assertEqual(True,b.isFull(1))
        b.space[1]= 1
        self.assertEqual(False,b.isFull(1))
        self.assertEqual(True,b.isFull(2))
        
        
    def testisTableauFull(self):
         '''Tests that function returns correct bool when all spaces are full'''
         b = BlackJack()
         b.space = self.setUp()
         self.assertEqual(True,b.isTableauFull())
         b.space[1] = 1
         self.assertEqual(False,b.isTableauFull())
    
class testcards(unittest.TestCase):
    
    def testtget_rank(self):
        '''cycles through all possible numbers and face cards to test'''
        rank = ['A','K','J','Q']
        for i in rank:
            card = Card(i,'S')
            self.assertEqual(i,card.get_rank())       
        for i in range(2,10):
            card = Card(i,'S')
            self.assertEqual(i,card.get_rank())
    def testtget_suit(self):
        '''cycles through all suits to test'''
        suit = ['S','C','H','D']
        for i in suit:
            card = Card('K',i)
        self.assertEqual(i,card.get_suit())
        
     
unittest.main()


        
                 
