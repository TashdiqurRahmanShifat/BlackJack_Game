from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing=True
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=''
        if rank.capitalize() in ranks:
            self.value=values[self.rank]
        else:
            print('Abbey Yaar')
    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    def __str__(self):
        deck_content=''
        for card in self.all_cards:
            deck_content+='\n'+'  '+card.__str__()
        return 'Deck contains 52 cards-'+'\n'+deck_content
    def shuffle(self):
        shuffle(self.all_cards)
    def dealing_card(self):
        return self.all_cards.pop()

class Hand:
    def __init__(self):
        self.cards=[]  
        self.value=0
        self.aces=0    #attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank.capitalize()=='Ace':
            self.aces+=1
    
    def adjust_for_ace(self):
        while self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1

class Chips:
    
    def __init__(self,total=100):
        self.total=total
        self.bet=0
        
    def win_bet(self):
        self.total+=self.bet
        
    
    def lose_bet(self):
        self.total-=self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("Enter your chips to bet:"))
        except:
            print("Enter an integer value")
            continue
        else:
            if chips.bet>chips.total:
                print("Oops!You do not have that chips.You have {} chips".format(chips.total))
            else:
                print("Thank you!")
                print("Your bet is {} chips".format(chips.bet))
                break


def hit(deck,hand):
    added_card=deck.dealing_card()
    hand.add_card(added_card)
    print("Added card-{}".format(added_card))
    hand.adjust_for_ace()


def show_some(player,dealer):
    print("In Dealers Hand")
    print("One Card Hidden")
    print(dealer.cards[1])
    print('\n')
    print("In Players Hand")
    for card in player.cards:
        print(card)

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:


        print('\n')
        x = input("Would you like to Hit or Stand? Enter 'h' for Hit or 's' for Stand:")
        
        if x[0].lower() == 'h':
            hit(deck,hand)




        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue


        break



def show_all(player,dealer):
    print("In Dealers Hand")
    for card in dealer.cards:
        print(card)
    
    print('\n')
    print("Dealer's total point {}".format(dealer.value))
    print('\n')
    print("In Players Hand")
    for card in player.cards:
        print(card)
    print('\n')
    print("Player's total point {}".format(player.value))
    print('\n')

def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def tie():
    print("Dealer and Player tie!")


while True:

    print('Welcome to BlackJack!')
    print('Here are some rules:')
    print('Get as close to 21 as you can without going over!')
    print('Dealer hits until she reaches 17. Aces count as 1 or 11.')

    print('\n')
    print('Allright!We are ready to play\n')

    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.dealing_card())
    player_hand.add_card(deck.dealing_card())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.dealing_card())
    dealer_hand.add_card(deck.dealing_card())

    # Setting up the Player's chips
    player_chips = Chips()    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    print('\n')

    show_some(player_hand,dealer_hand)

    while playing: 
        
        total_so_far=player_hand.value

        print("The sum of cards till now {}".format(total_so_far))

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        

        print('\n')

        if player_hand.value > 21:
            show_all(player_hand,dealer_hand)
            player_busts(player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    

        print("\nShowing both dealer & player cards--\n")

        show_all(player_hand,dealer_hand)
        

        if dealer_hand.value > 21:
            dealer_busts(player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)

        else:
            tie()  
    

    print("\nPlayer's winnings stand at",player_chips.total)
    


    new_game=''
    while new_game not in ['y','n']:
        new_game = input("Would you like to play another hand? Enter 'y' for Yes or 'n' No:")
  
    if new_game[0].lower()=='y':
        playing=True
        continue
    elif new_game[0].lower()=='n':
        print("Thanks for playing!")
        break 

            