import random
from IPython.display import clear_output

class Deck():
	def __init__(self):
		self.deck = {"nums" : ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q"],
					 "suit" : ['♠', '♣', '♥', '♦']}
		self.used_cards = []
		
class Player(Deck):

	def __init__ (self):
		Deck.__init__(self) #Is this right?
		self.hand = []
		self.score = 0
		self.busts = False
	#Create a constructor for the player class that will hold the hand,cards,and tally the score

	def deal(self):
		while len(self.hand) < 2:
			card = (random.choice(self.deck["nums"]), random.choice(self.deck["suit"]))
			if card not in self.used_cards:
				self.hand.append(card)
				self.used_cards.append(card)
	
	def hitPlayer(self):
		start_length = len(self.hand)
		while len(self.hand) == start_length:
			card = (random.choice(self.deck["nums"]), random.choice(self.deck["suit"]))
			if card not in self.used_cards:
				self.hand.append(card)
				print(str(card[0]) + card[1])
				
	# Get total score based on the hand the user/player is given
	def getScore(self):
		score = 0
		aces = 0
		
		for card in self.hand:
			if isinstance(card[0], int):
				score += card[0]
			elif card[0] in "KQJ":
				score += 10
			else:
				score += 11
				aces += 1
		while score > 21 and aces > 0:
			score -= 10
			aces -= 1
		self.score = score  #This updates the self.score of the player
		return score         #This gives a value that can be printed for the user's sake

	def bust(self):
		if self.score > 21:
			self.busts = True
			print("{} busted!".format(self.name))
			return True
		return False #This will return a Bool, can be used to break out of the game

class Human(Player):

	def __init__(self,name, bj = False):
		Player.__init__(self)
		self.name = name
		self.bj = bj
		self.hand = []
	
	def blackJack(self):
		if self.getScore() == 21:
			print("{} got Blackjack!!!".format(self.name))
			self.bj = True
				  
	def showHandPlayer(self):
		print('Here is your hand:')
		for card in self.hand:
			print(str(card[0]) + card[1])
				
				
class Dealer(Player):

	def __init__(self, name):
		Player.__init__(self)
		self.name = "Dealer"
				
	def showHand(self):
		print("Dealer's face-up card:")
		print(str(self.hand[0][0]) + self.hand[0][1])
		
	def showHandEnd(self):
		print("Here is the dealer's hand:")
		for card in self.hand:
			print(str(card[0]) + card[1])
	

class Game(Dealer, Human):

	#Define a constructor that will have a dealer,human,and players(the dealer and the human)
	def __init__(self, name):
		Dealer.__init__(self, name)
		Human.__init__(self, name)
		self.name = name
	
	#Define a method to display a message if the user/player wins
	# def winner(self):
		# if human_player.busts or dealer_player.score > human_player.score:
		#     print(dealer_player.name + ' wins!')
		# elif dealer_player.busts or human_player.score > dealer_player.score:
		#     print(human_player.name + ' wins!')
		# else:
		#     print('This hand was a tie.')
			  
	#Define a method to display a message if the user/player pushes

			  
	#Define a method to display a message if the user/player loses    

	
wanthit = 'y'
def main():
	human_player = Human(input("What is Your Name? "))
	dealer_player = Dealer('Dealer')
	game = Game('Tuesday')
			  
	#Ask the player how many decks they want to use - Then print the number of decks
	dealer_player.deal()
	human_player.deal()
	human_player.blackJack() #Make sure game ends
	human_player.showHandPlayer()
	if not human_player.bj:
		dealer_player.showHand()
	wanthit = 'y'
	while not human_player.busts and wanthit == 'y' and not human_player.bj: #Player's hits
		wanthit = input('Would you like to take a hit? (y/n) ')
		if wanthit.lower() == 'y':
			human_player.hitPlayer()
			human_player.getScore()
			human_player.bust()
	if dealer_player.getScore() < 17 and not human_player.busts and not human_player.bj:
		print('Dealer takes a hit!')
		dealer_player.hitPlayer()
		dealer_player.getScore()
		dealer_player.bust()
	dealer_player.showHandEnd()
	print(human_player.name + ' had a score of ' + str(human_player.score))
	print(dealer_player.name + ' had a score of ' + str(dealer_player.score))
	if human_player.busts or (dealer_player.score > human_player.score and not dealer_player.busts):
		print(f'{dealer_player.name} wins!')
	elif dealer_player.busts or (human_player.score > dealer_player.score and not human_player.busts):
		print(f'{human_player.name} wins!')
	else:
		print('This hand was a tie.')

		
	
	#HINT: Continue to ask player if they want a hit or if they want to end the game
	#Ask the player if they want a hit
	#If they do, add the value of the card to their game tally
	#If they stand, keep the game tally where it is - add to dealer only
	
	
			
		#Also add to the tally of the dealer while their tally is less than 16
		#If the dealer and player tally are the same - display that result
		#If dealer wins - display that result
		#If player wins - display that result
main()