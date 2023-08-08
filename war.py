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
#delete downwards this line incluso   
        #player1card,player2card=game(player1, player2)
        #if player1card > player2card:
    game(player1, player2)
        
        


# this is for test porpuses only mainly to check if the game pulls the right cards
#before completion this has to be deleted
def format_hand(hand):
    hand_str = ""
    for card in hand:
        hand_str += str(card) + "\n"
    return hand_str


# 4- make the game run without the war element
#every turn two cards are played #the player with the bigger card wins
def game(player1, player2):
    card1=[]
    card2=[]
    i=0
    while len(player1) > 0 and len(player2) > 0:
        print(f"player 1 has {len(player1)} cards and player 2 has {len(player2)} cards")
        #input("press enter to continue")
        i = i+ 1
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        print(f"player one has a {card1} player two has a {card2}")
        if card1.value > card2.value:
            print("player1 won this round")
            player1.append(card2)
            player1.append(card1)
        elif card1.value < card2.value:
            print("player2 won this round")
            player2.append(card2)
            player2.append(card1)
        if i==50 or i== 100 or i==200 or i==300 or i==400 or i ==500 or i ==600:
            input("press enter to continue")
        if i==1000 or i== 1500 or i==2000 or i==3000 or i==4000 or i ==5000 or i ==6000:
            input("press enter to continue")
        else:
            war(player1, player2, card1, card2)
            
        
            
    
    # this is for test porpuses only mainly to check if the game pulls the right cards
#before completion this has to be deleted     
    print(f"player 1 \n{format_hand(player1)}")
    print(f"player 2 \n{format_hand(player2)}")
#delete upwards from this line incluso

#5-make the war element of the game
#1 card down and one turned up
#compete to see whos the highest 
# #if they are equal restart
#def war():



if __name__ == "__main__":
    main()





#cards are ,4A ,4K ,4Q ,4J ,410 ,49 ,48 ,47 ,46 ,45 ,44 ,43, 4*2
 #in the battle the bigger the number allways wins


#maybe a list of random cards 
# #this list as to keep the same order through the game
#the player cannot see his cards









#6- create the winning condition(in this case the total absortion of the deck by one player?)
 #????


#7- give out a victory message
#You are victorious

