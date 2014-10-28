# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
flag = False
# flag stands for game over, 
win = 0
loss = 0
wind = 0
lossd = 0
count = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
        self.rank1 = []
        self.suit1 = []
        self.position = []
        self.hundred = 0
        self.count = -1

    def __str__(self):
        s = ""
        i = 0
        while i in range(0, len(self.hand)):
            s += (str(self.hand[i]) + " ")
            i += 1
        return s

    def add_card(self, card):
        self.hundred += 100
        self.position.append(self.hundred)
        self.rank1.append(card.get_rank())
        self.suit1.append(card.get_suit())
        self.hand.append(card.get_suit() + card.get_rank())

    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
    def get_value(self):
        self.value = 0
        ace_num=0
        for i in range(0, len(self.rank1)):
            if (self.rank1[i] == 'A' and self.value <= 10):
                ace_num += 1
                self.value+=1
            else:
                self.value += VALUES.get(self.rank1[i])
        for i in xrange(0,ace_num):
            if self.value<=11:
                self.value+=10
        return self.value

    def draw(self, canvas, p, r, s):
        card_location = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(r), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(s))
        canvas.draw_image(card_images, card_location, CARD_SIZE, [p[0] + CARD_CENTER[0], p[1] + CARD_CENTER[1]], CARD_SIZE)  
    
    def drawback(self, canvas, p):
        card_location1 = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_location1, CARD_BACK_SIZE, [p[0] + CARD_BACK_CENTER[0], p[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# define deck class
class Deck:
    def __init__(self):
        self.choice = -1
        del self.deck
        self.deck = []
        for i in range(1, 14):
            j = str(i)
            if (j == '1'):
                self.deck.append(Card('C', 'A').get_suit() + " " + Card('C', 'A').get_rank())
                self.deck.append(Card('S', 'A').get_suit() + " " + Card('C', 'A').get_rank())
                self.deck.append(Card('H', 'A').get_suit() + " " + Card('C', 'A').get_rank())
                self.deck.append(Card('D', 'A').get_suit() + " " + Card('C', 'A').get_rank())
            elif (j == '10'):
                self.deck.append(Card('C', 'T').get_suit() + " " + Card('C', 'T').get_rank())
                self.deck.append(Card('S', 'T').get_suit() + " " + Card('C', 'T').get_rank())
                self.deck.append(Card('H', 'T').get_suit() + " " + Card('C', 'T').get_rank())
                self.deck.append(Card('D', 'T').get_suit() + " " + Card('C', 'T').get_rank())
            elif (j == '11'):
                self.deck.append(Card('C', 'J').get_suit() + " " + Card('C', 'J').get_rank())
                self.deck.append(Card('S', 'J').get_suit() + " " + Card('C', 'J').get_rank())
                self.deck.append(Card('H', 'J').get_suit() + " " + Card('C', 'J').get_rank())
                self.deck.append(Card('D', 'J').get_suit() + " " + Card('C', 'J').get_rank())
            elif (j == '12'):
                self.deck.append(Card('C', 'Q').get_suit() + " " + Card('C', 'Q').get_rank())
                self.deck.append(Card('S', 'Q').get_suit() + " " + Card('C', 'Q').get_rank())
                self.deck.append(Card('H', 'Q').get_suit() + " " + Card('C', 'Q').get_rank())
                self.deck.append(Card('D', 'Q').get_suit() + " " + Card('C', 'Q').get_rank())
            elif (j == '13'):
                self.deck.append(Card('C', 'K').get_suit() + " " + Card('C', 'K').get_rank())
                self.deck.append(Card('S', 'K').get_suit() + " " + Card('C', 'K').get_rank())
                self.deck.append(Card('H', 'K').get_suit() + " " + Card('C', 'K').get_rank())
                self.deck.append(Card('D', 'K').get_suit() + " " + Card('C', 'K').get_rank())
            else:
                self.deck.append(Card('C', j).get_suit() + " " + Card('C', j).get_rank())
                self.deck.append(Card('S', j).get_suit() + " " + Card('C', j).get_rank())
                self.deck.append(Card('H', j).get_suit() + " " + Card('C', j).get_rank())
                self.deck.append(Card('D', j).get_suit() + " " + Card('C', j).get_rank())
    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        self.choice += 1
        return self.deck[self.choice]
 
    def __str__(self):
        return str(self.deck)

#define event handlers for buttons
def deal():
    global flag, deck, player, dealer, count, loss, wind, count
    count = 2
    flag = False
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    for i in range(0, 2):
        deal1 = deck.deal_card()
        split1 = deal1.split()
        card1 = Card(split1[0], split1[1])
        player.add_card(card1)
        deal2 = deck.deal_card()
        split2 = deal2.split()
        card2 = Card(split2[0], split2[1])
        dealer.add_card(card2)

def hit():
    global flag, loss, deck, player, dealer, wind, count
    if (count < 5 and flag==False):
        if (player.get_value() <= 21):
            print(count)
            count += 1
            hit = deck.deal_card()
            split = hit.split()
            card = Card(split[0], split[1])
            player.add_card(card)
            if (player.get_value() > 21):
                count = 6
                flag=True
                if player.get_value()>21:
                    loss+=1
                    wind+=1
                elif dealer.get_value()>21:
                    win+=1
                    lossd+=1
                elif dealer.get_value()>=player.get_value():
                    loss+=1
                    wind+=1
                else:
                    win+=1
                    lossd+=1

def stand():
    global flag, win, loss, wind, lossd
    if (flag == False and player.get_value() <= 21):
        countd = 0
        while ((dealer.get_value() < 17) and (countd<5)):
            hit = deck.deal_card()
            split = hit.split()
            card = Card(split[0], split[1])
            dealer.add_card(card)
            countd+=1
        flag = True
        if player.get_value()>21:
            loss+=1
            wind+=1
        elif dealer.get_value()>21:
            win+=1
            lossd+=1
        elif dealer.get_value()>=player.get_value():
            loss+=1
            wind+=1
        else:
            win+=1
            lossd+=1
            
# draw handler    
def draw(canvas):
    global flag, deck, player, dealer
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Player's Hand:" + str(player.get_value()), (10, 350), 12, "Yellow")
    canvas.draw_text("Player", (40, 150), 12, "White")
    canvas.draw_text("Dealer", (40, 250), 12, "White")
    canvas.draw_text("Player Wins:" + str(win), (455, 350), 12, "White")
    canvas.draw_text("Player Losses:" + str(loss), (455, 380), 12, "White")
    canvas.draw_text("Dealer Wins:" + str(wind), (300, 350), 12, "White")
    canvas.draw_text("Dealer Losses:" + str(lossd), (300, 380), 12, "White")
    canvas.draw_text("BlackJack", (180, 40), 30, "Red")
    if (flag == False and player.get_value() <= 21):
        canvas.draw_text("Hit or Stand?", (180, 550), 20, "Black")
    for i in range(0, len(player.position)):
        player.draw(canvas, [player.position[i], player.position[0]], player.rank1[i], player.suit1[i])
    if (flag == True):
        dealer.draw(canvas, [dealer.position[0], dealer.position[1]], dealer.rank1[0], dealer.suit1[0])
    else:
        dealer.drawback(canvas, [dealer.position[0], dealer.position[1]])
    for j in range(1, len(dealer.position)):
        dealer.draw(canvas, [dealer.position[j], dealer.position[1]], dealer.rank1[j], dealer.suit1[j])

    if ((player.get_value() > 21) and (flag == True)):
        canvas.draw_text("Player is Busted", (180, 480), 20, "Black")
        canvas.draw_text("New Deal?", (180, 550), 20, "Black")
    elif ((player.get_value() == dealer.get_value()) and (dealer.get_value() >= 17) and (flag == True)):
        canvas.draw_text("Tie!! Dealer Wins", (180, 480), 20, "Black")
        canvas.draw_text("Dealer's Hand:" + str(dealer.get_value()), (10, 380), 12, "Yellow")
        canvas.draw_text("New Deal?", (180, 550), 20, "Black")
    elif (dealer.get_value()>21) and (flag==True):
        canvas.draw_text("Dealer is Busted!! Player Wins", (180, 480), 20, "Black")
        canvas.draw_text("Dealer's Hand:" + str(dealer.get_value()), (10, 380), 12, "Yellow")
        canvas.draw_text("New Deal?", (180, 550), 20, "Black")
    elif ((dealer.get_value() > player.get_value()) and (dealer.get_value() >= 17) and (flag == True)):
        canvas.draw_text("Dealer Wins", (180, 480), 20, "Black")
        canvas.draw_text("Dealer's Hand:" + str(dealer.get_value()), (10, 380), 12, "Yellow")
        canvas.draw_text("New Deal?", (180, 550), 20, "Black")
    elif ((player.get_value() > dealer.get_value()) and (dealer.get_value() >= 17) and (flag == True)):
        canvas.draw_text("Player Wins", (180, 480), 20, "Black")
        canvas.draw_text("Dealer's Hand:" + str(dealer.get_value()), (10, 380), 12, "Yellow")
        canvas.draw_text("New Deal?", (180, 550), 20, "Black")

# deal an initial hand
player = Hand()
dealer = Hand()
deck = Deck()
deck.shuffle()
for i in range(0, 2):
    deal1 = deck.deal_card()
    split1 = deal1.split()
    card1 = Card(split1[0], split1[1])
    player.add_card(card1)
    deal2 = deck.deal_card()
    split2 = deal2.split()
    card2 = Card(split2[0], split2[1])
    dealer.add_card(card2)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()