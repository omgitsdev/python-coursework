#Jingru Zhu and Dev Sethi
#CIT 590, Fall 2013

from cards import *
class BlackJack(object):
    '''creates the board; draws, places, and discards cards, calculates score'''
    def __init__(self):
        '''Creates a dictionaries of size 16 and 4 to hold the playing field and discard pile, respectively'''
        self.space = {}
        self.trash = {}
        for i in range(1,17):
            self.space[i] = i
        for i in range(17,21):
            self.trash[i] = i


    def displayState(self):
        '''Displays solitarie blackjack board in proper format; fills each space with either
        a number (if no card has been played there) or with the rank/suit of the card'''
        print ('Board: \n')
        for i in range(1,6):
            if (len(str(self.space[i]))== 1):
                print '[  ' + str(self.space[i]) + '] ',
            elif (len(str(self.space[i]))== 2):
                print '[ ' + str(self.space[i]) + '] ',
            else:
                print '[' + str(self.space[i]) + '] ',
        print '\n'
        for i in range(6,11):
            if (len(str(self.space[i]))== 1):
                print '[  ' + str(self.space[i]) + '] ',
            elif (len(str(self.space[i]))== 2):
                print '[ ' + str(self.space[i]) + '] ',
            else:
                print '[' + str(self.space[i]) + '] ',
        print '\n'
        print '      ',
        for i in range(11,14):
            if (len(str(self.space[i]))== 1):
                print '[  ' + str(self.space[i]) + '] ',
            elif (len(str(self.space[i]))== 2):
                print '[ ' + str(self.space[i]) + '] ',
            else:
                print '[' + str(self.space[i]) + '] ',
        print '\n'
        print '      ',
        for i in range(14,17):
            if (len(str(self.space[i]))== 1):
                print '[  ' + str(self.space[i]) + '] ',
            elif (len(str(self.space[i]))== 2):
                print '[ ' + str(self.space[i]) + '] ',
            else:
                print '[' + str(self.space[i]) + '] ',
        print '\n Discard'
        for i in range(17,21):
            if (len(str(self.trash[i]))== 1):
                print '[  ' + str(self.trash[i]) + '] ',
            elif (len(str(self.trash[i]))== 2):
                print '[ ' + str(self.trash[i]) + '] ',
            else:
                print '[' + str(self.trash[i]) + '] ',


    def placeCard(self, c, p):
        '''assigns passed card to passed location by assigning the card value to the space key'''
        self.space[p] = c

    def trashCard(self, c, p):
        '''assigns passed card to passed location by assigning the card value to the space key'''
        self.trash[p] = c

    def isFull(self,p):
        '''Checks to see if a card has already been played on the passed space
        the spaces are initialized to integers so if that changes, it means it was replaced
        by an instance of Card'''
        if (p < 17):
            return (type(self.space[p]) != int)
        else:
            return (type(self.trash[p]) != int)

    def isTableauFull(self):
        '''Checks if all the playing spaces have been occupied, disregards the discard pile'''
        count = 0
        for i in range(1,17):
            if self.isFull(i):
                count += 1
        if  count == 16:
            return True
        else:
            return False

    def rowScore(self,r):
        '''Calculates the score of the passed row; modifies calculation based on the
        row because some have 5 cards and some have 3 cards'''
        score = 0
        if r < 3:
            for i in range(5*r-4, 5*r+1):
                score += self.space[i]
            return self.scoreRange(False,score)
        else:
            for i in range(3*r+2, 3*r+5):
                score += self.space[i]
            return self.scoreRange(False,score)



    def colScore(self,c):
        '''Calculates the score of the passed column; modifies calculation based on the
        column because some have 5 cards and some have 2 cards'''
        score = 0
        if c == 1 or c == 5:
            score = self.space[c] + self.space[c+5]
            return self.scoreRange(True,score)
        else:
            score = self.space[c] + self.space[c+5] + self.space[c+9] + self.space[c+12]
            return self.scoreRange(False,score)



    def scoreRange(self,isShortColumn,score):
        '''Converts the sum of the card ranks and determines the game-specific score for that row/column
        modifies calculation for two-card columns to allow for 10 point blackjack'''

        if score >= 22:
            score = 0
        elif score == 21:
            if isShortColumn:
                score = 10
            else:
                score = 7
        elif score == 20:
            score = 5
        elif score == 19:
            score = 4
        elif score == 18:
            score = 3
        elif score == 17:
            score = 2
        elif score <=16:
            score = 1

        return score

    def scoreGame(self):
        '''Compiles score based on the Card instances in the spaces dictionary of the blackjack instance'''
        rowList = [1, 2, 3, 4]
        colList = [1, 2, 3, 4, 5]
        score = 0
        for i in rowList:
            score += self.rowScore(i)
        for i in colList:
            score += self.colScore(i)
        return score


    def aceCalc(self):
        """This function count the difference value of ace
           and finds out the maximum value of the whole table"""
        countA = 0
        """if there is no ace in certain position,
           then do not count"""
        ace = [17,18,19,20]
        aceLocation = []
        #convert all face to 10
        for i in range(1,17):
            temp = self.space[i].get_rank()
            if temp == 'J' or temp == 'K' or temp == 'Q':
                self.space[i] = 10
            elif temp == 'A':
                countA +=1
                ace[countA]=i
            else:
                self.space[i] = temp
        scoreList = []
        aceValue = [1,11]

        #nested loops to run through every combination of the values for Ace.
        for i in aceValue:
            for j in aceValue:
                for k in aceValue:
                    for l in aceValue:
                        self.space[ace[0]] = i
                        self.space[ace[1]] = j
                        self.space[ace[2]] = k
                        self.space[ace[3]] = l
                        scoreList.append(self.scoreGame())  #List of the score of every combination
        #print "\n",scoreList
        #print "\n", ace, countA, max(scoreList)
        return max(scoreList)
        #return max(scoreList)






def play():
    '''initiates the game'''

    #Initiation of deck and blackjack
    d = Deck()
    b = BlackJack()
    d.shuffle()
    b.displayState()

    print '\n'
    while (b.isTableauFull() == False):
        tempCard = d.deal()
        flag = True
        print '\n'
        print "Place this card: ",
        print tempCard
        while (flag):
            """Ask users to place the card"""
            try:
                p = int(raw_input("Select space (1-20): "))
            except ValueError:
                p = -1
            if p >= 1 and p <= 20:
                if b.isFull(p)== False:
                    if (p<17):
                        b.placeCard(tempCard,p)
                    elif(p<21):
                        b.trashCard(tempCard,p)
                    b.displayState()
                    flag = False
                else:
                    print "Invalid move: Space is already occupied."
                    flag = True
            else:
                print "Invalid input: Please enter a number in (1-20):"
                flag = True
    print '\n'
    print "The Table is full, Start Calculating.\n "
    print "Your score is: ",b.aceCalc()
