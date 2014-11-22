#Jingru Zhu and Dev Sethi
#CIT 590, Fall 2013

import random  # needed for shuffling a Deck

class Card(object):
    #the card has a suit - 'S','C','H', 'D'
    # the card has a rank
    
    def __init__(self, r, s):
        '''Initiates instance of card with supplied rank and suit'''
        self.r = r
        self.s = s
        #implement
        #where r is the rank, s is suit


    def __str__(self):
        return str(self.r) + str(self.s)

    def get_rank(self):
        '''returns rank of card instance'''
        return self.r
    def get_suit(self):
        '''returns suit of card instance'''
        return self.s

   
class Deck(object):
    """Denote a deck to play cards with"""
     
    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits
           1 is A, 11 is J, 12 is Q, 13 is K """
        suit = ['S','C','H','D']
        self.cards = []
        face = ['A','J','Q','K']
        for i in range(2,11):
            for j in suit:   
                self.cards.append(Card(i,j))
        for i in face:
            for j in suit:
                self.cards.append(Card(i,j))

    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)

    def get_deck(self):
        raise NotImplementedError

    def deal(self):
        '''simulates dealing by popping out a card instance from the deck instance'''
        return self.cards.pop()
        # get the last card in the deck
        # simulates a pile of cards and getting the top one
        #raise NotImplementedError
    
    def __str__(self):
        """Represent the whole deck as a string for printing"""
       #the deck is a list of cards
       #this function just calls str(card) for each card in list
       # put a '\n' between them
        deckString = ''
        for i in range(0,len(self.cards)):
            deckString += str(self.cards[i])
            deckString += '\n'

        return deckString





    
