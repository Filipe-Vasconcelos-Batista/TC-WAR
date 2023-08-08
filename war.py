import random

#creating the card game war in python



#each player gets half of the cards in the beggining (26)

#2- create a object class for the cards (can be just one with various definitions)
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value= value
   
    

#1- create a object class for the deck 
#deck has 52 cards
    def __str__(self):
        if self.value == 11:
            value_str = "Jack"
        elif self.value == 12:
            value_str = "Queen"
        elif self.value == 13:
            value_str = "King"
        elif self.value == 14:
            value_str = "Ace"
        else:
            value_str = self.value
        return f"{value_str} of {self.suit}"

card1=Card("hearts",14)
print(card1)

class Deck:
    def __init__(self):
        self.cards=[]   
        self.suits=["hearts","clovers","spades" ,"diamonds"]
        self.values=list(range(2,15))
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))
                random.shuffle(self.cards)  
        
        
    def __str__(self):
        cards_str = ""
        for card in self.cards:
            cards_str += str(card) + "\n"
        return cards_str
                
def main():
    #26 cards for each player
    deck = Deck()
    half = len(deck.cards) // 2
    player1 = deck.cards[:half]
    player2 = deck.cards[half:]
    #game(player1, player2)
    
    print(f"player 1 \n{format_hand(player1)}")
    print(f"player 2 \n{format_hand(player2)}")
    

def format_hand(hand):
    hand_str = ""
    for card in hand:
        hand_str += str(card) + "\n"
    return hand_str

if __name__ == "__main__":
    main()





#cards are ,4A ,4K ,4Q ,4J ,410 ,49 ,48 ,47 ,46 ,45 ,44 ,43, 4*2
 #in the battle the bigger the number allways wins

#3-make the random distribution of the 52 cards
#26 cards for each player
#maybe a list of random cards 
# #this list as to keep the same order through the game
#the player cannot see his cards





# 4- make the game run without the war element
#every turn two cards are played #the player with the bigger card wins
#def game():

#5-make the war element of the game
#1 card down and one turned up
#compete to see whos the highest #if they are equal restart
#def war():

#6- create the winning condition(in this case the total absortion of the deck by one player?)
 #????


#7- give out a victory message
#You are victorious
# this is for test porpuses only mainly to check if the game pulls the right cards
#before completion this has to be deleted
