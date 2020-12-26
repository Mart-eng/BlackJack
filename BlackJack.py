#BlackJack
import random

class BlackJack:

    def __init__(self):

        self.deck = Deck()
        self.UI = UserInterface()
        self.stats = Statistics()

        
    def playGame(self):
        
        self.UI.printIntro()
        self.deck.drawCards()
        
        try:
            while True:
                self.playRound()
                self.stats.roundsplayed += 1
                print()
                if self.UI.newRoundQuestion() == False:
                    print('Have a good day!')
                    self.UI.displayGameScore(self.deck.endScore())      #end score, avg of hands
                    self.UI.displayStats(self.stats.roundsplayed)                               
                    break
                
                
        except IndexError:
                self.UI.displayScore(self.deck.score()) #round score    
                print("The deck ran out of cards!")
                self.UI.displayGameScore(self.deck.endScore())  
                self.UI.displayStats(self.stats.roundsplayed)

        except ZeroDivisionError:
                print("Your score is ",self.deck.score())
                self.UI.displayStats(self.stats.roundsplayed)



    def playRound(self):
        while True:
            self.deck.drawCards()
            self.UI.displayHand(self.deck.getHand())
            print()
            self.UI.displayScore(self.deck.score())
            self.deck.scoreTwo.append(self.deck.score())
    
            if (self.UI.drawQuestion() == False):
                self.UI.displayScore(self.deck.score())
                self.deck.playercards = []
                break       



class UserInterface:

    def printIntro(self):
        print("Da rules: This game is called Blackjack.")
        print("There are 52 cards: Spades, Clubs, Diamonds and Hearts each numbered 1 - 13")
        print("You can choose to draw a card each round.")
        print("If the numbers add up and they are less then 12 or more than 21, your score is 0.")


    def newRoundQuestion(self):
        'Returns True to keep playing, False to stop'
        playAgain = input("Do you want to play another round? (Yes or No): ")
        playAgain = playAgain.lower()


        return (playAgain[0] == 'y')

    def displayScore(self, score):
        print ("Your score for this round is: ", score) # {0:0>2}).format(score)

    def displayGameScore(self, score):
        print ("Your score for this game is: ", score)
        

    def displayHand(self, hand):
        print ("Your hand is currently: ",hand)

    def drawQuestion(self):
        drawAgain = input("Do you want to draw again? (Yes or No): ")
        drawAgain = drawAgain.lower()

        return (drawAgain[0] == 'y')

    def displayStats(self,roundsplayed):
        print("Rounds played: ",roundsplayed)
      

class Deck():
    
    def __init__(self):
        self.deck = []
        self.playercards = []
        self.types = ["Spades ","Clubs ","Diamonds ","Hearts "]
        self.number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.scoreTwo = []
        for types in self.types:
            for number in self.number:
                self.deck.append((types + str(number)))

    def getDeck(self):
        return self.deck

    def getHand(self):
        return self.playercards

    def drawCards(self):
        #Drawing cards
            x = random.choice(self.deck)
            self.playercards.append(x)
            self.deck.remove(x)
        
    def score(self):
        "The score for 1 round of play"
        total = 0
        roundScore = 0
        for card in self.playercards:
            roundScore = int(card[-2:])
            total = total + roundScore

        if total > 21 or total < 12:
            total = 0
            
        return total
    

    def endScore(self): 
        "The score for the end of the game"
        totalScore = 0
        for score in self.scoreTwo:
            totalScore = totalScore + score

        endscore = totalScore / len(self.scoreTwo)     
        return endscore
        
class Statistics:

    def __init__(self):
        self.roundsplayed = 0
        
def main():
    game = BlackJack()
    game.playGame()

main()     
