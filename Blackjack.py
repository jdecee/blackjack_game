import random

class Game:

    def __init__(self):
        self.dealer = Player(user=False)
        values = [i for i in range(1, 14)]
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.deck = [Cards(v, s) for v in values for s in suits]
        self.rand_hand()
        self.players = [self.dealer]

    def add_player(self, player):
        self.players.insert(0, player)


    def rand_hand(self):
        assert (len(self.deck) == 52)
        random.shuffle(self.deck)

    def start_hand(self):
        self.rand_hand()
        for player in self.players:
            self.deal(player)
            self.deal(player)

    def deal(self, player):
        player.hit(self.deck.pop())
           
class Player:

    def __init__(self, initial_balance=0, user=True):
        self.stand = False
        self.user = user
        self.hand = []
        self.balance = initial_balance
        self.total = 0
         
    def hit(self, card):
        self.hand.append(card)
        self.stand = False

    def hand_status(self):
        for card in self.hand:
            self.total = self.total + card.values
        print("hand value = " + str(self.total))
        if self.total == 21 and len(self.hand) == 2:
            return "Blackjack"
        elif self.total > 21:
            return "Busted"
        else:
            return self.total
        
    

    def stand(self):
        self.stand = True

    def place_bet(self):
        while True:
            if self.balance > 0:
                user_bet = int(input(f'Your remaining balance is {self.balance} dollars, How much would you like to bet? '))
                if user_bet <= self.balance:
                    self.balance -= user_bet
                    break
                print("Bet exceeds balance")
        return user_bet
        
            
 # Check score   
    def check_score(self):
        pass

 # Show Cards   
    def show_cards(self):
        pass



class Cards:
   
    def __init__(self, values, suit):
        self.values = values
        self.suit = suit



    
# program

def run():
    gameOn = Game()
    us = Player(100)
    gameOn.add_player(us)
    wager = us.place_bet()
    gameOn.start_hand()
    test = us.hand_status()
    print(test)
    while True:
        choice = input("Card? ")
        if choice == "Yes":
            gameOn.deal(us)
            test_1 = us.hand_status()
            if test_1 == "Busted":
                break
            elif test_1 == "Blackjack":
                us.balance = us.balance + 2.5 * wager
            else:
                pass
        else:
            pass
    print("Thanks for playing!")



run()
