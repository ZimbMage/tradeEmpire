import random
import duck
import resources
import cards






#####
          #[0,0,0,0,0,0,0,0,0]
green =    [1,0,0,0,0,0,0,0,0]
white =    [0,1,0,0,0,0,0,0,0]
brown =    [0,0,1,0,0,0,0,0,0]
	
blue =     [0,0,0,1,0,0,0,0,0]
yellow =   [0,0,0,0,1,0,0,0,0]
black =    [0,0,0,0,0,1,0,0,0]

hexagon  = [0,0,0,0,0,0,1,0,0]
vp =       [0,0,0,0,0,0,0,1,0]
ships =    [0,0,0,0,0,0,0,0,1]


green_cube = 0
white_cube = 1
brown_cube = 2


blue_cube =  3
yellow_cube= 4
black_cube = 5

hex_cube =   6
vp_cube =    7
ship_cube =  8

####

#card typeing:
starting_convter = 0
planet = 1 

## i want a way to create a bunch of 'colonies'
## to create one, i need to create a new convter, name it, then add it to 
## will move to a pre created list of all plantes, or just add a random flip+ flip cost. 

def random_small_Output():
		x = random.randint(0,2)
		if x == 0 :
			return [1,0,0]
		elif x == 1:
			return [0,1,0]
		else:
			return [0,0,1]    	

def add_start_planets (player):
		for addPlant in range (0,player.start_planet):
			addPlant = cards.convter(("planet"+str(addPlant)),[],random_small_Output(),planet)
			player.convters.append(addPlant)
			player.planet_Count += 1
		print(str(player.planet_Count) + " " + player.my_name)

def add_planets (player):
		for addPlant in range (player.planets_perTurn):
			if player.planet_Count<player.maxplanet_count:
				addPlant = cards.convter(("planet"+str(addPlant)),[],random_small_Output(),planet)
				player.convters.append(addPlant)
				player.planet_Count += 1
		print(str(player.planet_Count) + " " + player.my_name)


def planet_phase(players):
	print("add more planets")
	for player in players:
		add_planets(player)






class player:
	def __init__(self,my_cubes,my_convters, name,starting_planet_count,planets_per_Turn, MaxP):   # load up all starting things 
		self.cubes = my_cubes
		self.convters = my_convters
		self.start_planet = starting_planet_count 
		self.planets_perTurn = planets_per_Turn
		self.planet_Count = 0
		self.maxplanet_count = MaxP
		self.my_name = name


## need to write a function that figures out what cubes i will not use with my curent convters. -> create a list of all convter costs. 
	def convter_cost_calc(self):
		print(self.my_name + " curent convter needs")
		
		self.upcomeingCosts = [0]*9
		
		for convter in self.convters:
		
			for i in range(len(convter.costs)):
				if convter.trade_for_me == True:
					self.upcomeingCosts[i] = self.upcomeingCosts[i] + convter.costs[i]
		
		for i in range(len(self.upcomeingCosts)):
			self.upcomeingCosts[i] = self.cubes.my_cubes[i]-self.upcomeingCosts[i]
		

		print("what cubes do i have in list form")
		print(self.cubes.my_cubes)
		print("Extra and needs")
		print(self.upcomeingCosts)
		print(" ")




	def convter_cost_calc_silent(self):
		#print(self.my_name + " curent convter needs")
		self.upcomeingCosts = [0]*9
		for convter in self.convters:
			for i in range(0,len(convter.costs)):
				self.upcomeingCosts[i] = self.upcomeingCosts[i] + convter.costs[i]
		for i in range(0,len(self.upcomeingCosts)):
			self.upcomeingCosts[i] = self.cubes.my_cubes[i]-self.upcomeingCosts[i]
		#print("what cubes do i have in list form")
		#print(self.cubes.my_cubes)
		#print("Extra and needs")
		#print(self.upcomeingCosts)
		#print(" ")
		

def trade_offer(player_offer,Player_reciveingOffer):
	global tradecount
	global tradefail_count

	my_needs = []
	my_trades = []
	
	their_needs = []
	their_trades = [] 
	
	what_I_want = -99
	#what_I_offer = -99
	what_they_want = -99

	index_of_cube_i_want = -99
	index_of_their_cube = -99

	
	print("start of trade" + str(tradecount+ tradefail_count))
	print("####################################")

	print(player_offer.my_name)
	print("what upcomeingCosts do i have?")
	print(player_offer.upcomeingCosts)
	for i in range(len( player_offer.upcomeingCosts)):
		if player_offer.upcomeingCosts[i]<0	:     ## if this value is less then zero, it means i need that type of cube to run my convters. 
			my_needs.append(i)
		elif player_offer.upcomeingCosts[i]>0 and i < 7:
			my_trades.append(i)
		 	
	print("this is what i need")		
	print(my_needs)
	print(" this is what i can offer ")
	print(my_trades)

	for i in range(len(Player_reciveingOffer.upcomeingCosts)):
		if Player_reciveingOffer.upcomeingCosts[i]<0:
			their_needs.append(i)
		elif Player_reciveingOffer.upcomeingCosts[i]>0 and i< 7 :
			their_trades.append(i)

	print(Player_reciveingOffer.my_name)
	print("this is what they have coming up")
	print(Player_reciveingOffer.upcomeingCosts)
	print("this is what they need")
	print(their_needs)
	print("this is what they can trade away")
	print(their_trades)

	if len(my_needs)>0 :
		what_I_want =	random.randint(0,len(my_needs)-1) 
		what_I_want = my_needs[what_I_want]
		print("this is what i want")
		print(what_I_want)
		
		# do they have what cube i want? 
		for i in range(len(their_trades)):
			if their_trades[i] == what_I_want:
				## they want my item at index i
				print("they have what i want")
				index_of_cube_i_want = i 
		if  index_of_cube_i_want == -99:
			print("they dont have what i want")



	if len(their_needs) > 0 :
		what_they_want= random.randint(0,len(their_needs)-1)
		what_they_want = their_needs[what_they_want]
		print("what they want this time ")
		print(what_they_want)

		# do i have what they want?
		for i in range(len(my_trades)):
			if my_trades[i] == what_they_want:
				## they want my item at index i
				index_of_their_cube = i 
				print("i have what they want")
		if index_of_their_cube == -99:
			    print("I dont have what i want")


	##### now i have what they want and what i want. lets print that. 
	print("what i want: " + str(what_I_want)	)		
	print("what they want:" + str(what_they_want) )




	##### for now, always say yes. no real rejection logic. 
	## this is a trade in action....
	if index_of_cube_i_want != -99 and index_of_their_cube !=-99:   ## this check makes sure they can trade what i want by finding it on their can offer list. 
		## we can and will trade 1 for 1. 
		# i lose and gain one cube.
		#print(player_offer.cubes.cube_Count())
		player_offer.cubes.addcubes([what_I_want,what_they_want], [1,-1])
		Player_reciveingOffer.cubes.addcubes([what_I_want,what_they_want], [-1,1])
		#print("Post swap")
		#print(player_offer.cubes.cube_Count())
		player_offer.convter_cost_calc_silent()
		Player_reciveingOffer.convter_cost_calc_silent()
		print("trade happned")
		tradecount = tradecount +1 
		
		## check to see if ppl need to start tradeing for new items:
		addNewNeed = True
		for i in player_offer.upcomeingCosts:
			print(i)
			if i <0:
				addNewNeed = False	# no update
		if addNewNeed == True:
			print("adding need for:" + player_offer.my_name)
			think_convtersToFire(player_offer.convters)
		else:
			print(player_offer.my_name + " no need for new need")


		addNewNeed = True
		for i in Player_reciveingOffer.upcomeingCosts:
			print(i)
			if i <0:
				addNewNeed = False	# no update
		if addNewNeed == True:
			print("adding need for :" + Player_reciveingOffer.my_name)
			think_convtersToFire(Player_reciveingOffer.convters)
		else:
			print(Player_reciveingOffer.my_name + " no need for new need")


	else :
		print("no trade")
		tradefail_count = tradefail_count + 1 
	print("End of trade")
	print("####################################")




def think_convtersToFire(convters):  ## need to fire this when i want to add a new convter to hunt for
	convter_value = -99
	trade_for_this_convter = cards.convter("placeholder",[99,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],starting_convter)
	#trade_for_this_convter
	
	for convter in convters:
		#print(convter.name)
		if convter.convter_type == planet:
			#print("planet")
			pass
		elif convter.convter_value() > convter_value and convter.trade_for_me == False:
			trade_for_this_convter = convter
			convter_value = convter.convter_value()
		#	print("sup")
		else:
			pass
			#print("keep tradeing for curent card")
	print(trade_for_this_convter.name)
	trade_for_this_convter.trade_for_me = True  # now trying to get cubes for this convter as well. 
	print(trade_for_this_convter.trade_for_me)



#self,brown,w,green,blue,y,black,h,ship)
p1cubes = resources.cubes(2,1,1,1,2,2,0,0,4)   # red
p2cubes = resources.cubes(3,2,3,1,1,1,1,0,0)   # brown 
p3cubes = resources.cubes(2,4,5,0,0,2,0,0,1) #green
p4cubes = resources.cubes(1,3,0,1,1,0,1,0,1) #yellow 

p1cubes.cube_Count()
#p2cubes.cube_Count()

print('******')

#def printCubes():
#	for someCube in myCubes:
#		someCube.cube_Count()



convters = []
p2convters = []
p3convters = []
p4convters =[]

player1 = player(p1cubes,convters,"KJASJAVIKALMM (two fleet bid ppl)",2,2,6) ## thats much more clear then "bob"
player2 = player(p2cubes,p2convters,"KT'ZR'TY'RTL (BUG ppl)",1,1,500)
player3 = player(p3cubes,p3convters,"Caylion",2,2,8)
player4 = player(p4cubes,p4convters,"Faderan",1,1,4)



gamePlayers = [player1,player2,player3,player4]

#convters.append()
print("add Starting planets")
for player in gamePlayers:
	add_start_planets(player) ## add x random small planets


#print(convters)
#printCubes()

#test = convter('three small for two large',[0,2,0],[0,0,0,0,1])
#test.convter_output()
#anotherTest = convter('testRules',[0,0,0,0,2], [0,1,1,1])

###### need to manage createing conveters via XML later. for now, all by hand. 
#cube_names = [green_name,white_name, brown_name,blue_name,yellow_name,black_name,hexagon_name,vp_name,ships_name]  ## this is good use of the stirngs above, i think. 
#[sum(x) for x in zip(list1, list2)]


#someTest = [sum(x) for x in zip(green,green,green,white,ships)]
#print(zip(green,green,green,white,ships))



### wonder what a beter way to create the convters is?



red1 = cards.convter("red1",[],[0,0,2,0,0,0,0,0,3],starting_convter)
player1.convters.append(red1)
#red1.convter_output()

red2 = cards.convter("red2",[0,0,0,2,0,0,0,0,0],[1,0,0,0,0,0,0,0,4],starting_convter)
player1.convters.append(red2)

red3 = cards.convter("red3",[0,0,4,0,0,0,0,0,0],[0,1,0,1,1,1,0,0,0],starting_convter)
player1.convters.append(red3)

brown1 = cards.convter("brown1",[],[0,0,0,0,0,0,1,0,1],starting_convter)
player2.convters.append(brown1)

brown2 = cards.convter("brown2",[5,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,0,0,4],starting_convter)
player2.convters.append(brown2)

brown3 = cards.convter("brown3",[0,0,0,0,0,0,1,0,0],[1,1,2,0,0,0,0,0,0],starting_convter)
player2.convters.append(brown3)


green1 = cards.convter("green1",[],[sum(x) for x in zip(green,green,green,white,ships)],starting_convter) # not awful! but not great | readable 
player3.convters.append(green1)

green2 = cards.convter("green2",[0,0,0,2,0,0,0,0,0],[0,1,0,0,0,1,0,0,2],starting_convter)
player3.convters.append(green2)

green3 = cards.convter("green3",[2,0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0],starting_convter)
player3.convters.append(green3)

green4 = cards.convter("green4",[0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0],starting_convter)
player3.convters.append(green4)


yellow1 = cards.convter("yellow1",[0,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,1],starting_convter)
player4.convters.append(yellow1)

yellow2 = cards.convter("yellow2",[0,4,0,0,0,0,0,0,0],[1,0,0,0,0,1,1,0,0],starting_convter)
player4.convters.append(yellow2)

yellow3 = cards.convter("yellow3",[0,0,2,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,2],starting_convter)
player4.convters.append(yellow3)

yellow4 = cards.convter("yellow4",[3,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,0],starting_convter)
player4.convters.append(yellow4)


#print(player1.convters)





#### run all convters

# self.convters = my_convters
#self.cubes = my_cubes
#self.convters = my_convters
#self.start_planet = starting_planet_count 
#self.planet_Count = 0
#self.my_name = name




def run_convters(players):
		for player in players:

			print('******* running convters for ' + player.my_name  + ' *******')
			#print('test something(player cubes)')
			#print(player.cubes)
			#print("clean convter share bug")
			
			player.cubes.fixConvterShareBug() ## What is this? | nice bug fix.....

			print("run all of my convters')")
		

			for the_convter in player.convters:
			#	aConvter.convter_name()
				#print('run a convter')
				the_convter.RunConvter(player.cubes)
				#print('end a convter')
				print('')
			print("cube count:")
			player.cubes.update_postEcon()
			player.cubes.cube_Count()
			print('*end of convters*')
			print("")
		print("end of all convters")	





## ok, here i can see what both have extra of and need, now how to turn that into a trade offer. (dont worry about fair offer yet,lets just do 1 cube for 1 cube.)

tradecount = 0
tradefail_count = 0




def set_free_to_true(players):
	for player in players:
		for convter in player.convters:
			#print(convter.name)
			print(convter.costs)
			print([0]*9)

			if convter.costs ==  [0]*9:
				convter.trade_for_me=True
				print(convter.name)
				#print("WORKING")
			else:
				pass
				#print("no update")



def reset_convters_toTradeFor(players):
	for player in players:
		for convter in player.convters:

			convter.trade_for_me = False;

    

def TradePhase(trades):
	print ( " Start of Trade Phase")

	for player in gamePlayers:
		player.convter_cost_calc()

#player1.convter_cost_calc()

	for unused in range(trades):
		trade_pair = random.sample(gamePlayers,2)
		trade_offer(trade_pair[0],trade_pair[1])


	print("trades")
	print(tradecount)

	print("trades done, post trade info")
	for player in gamePlayers:
		player.convter_cost_calc()

print("end of pre game setup")
print(" ")
print(" ")
print(" ")






## runs the game, takes actions, 
def PlayTradeEmpireSimulation(turns, trades): 
	for unused in range(turns):
		# how many trades should i try to do? 

		# clean up stuff
		reset_convters_toTradeFor(gamePlayers)
		set_free_to_true(gamePlayers)
		
		for player in gamePlayers:
			print(player.my_name + " updated trade list")
			think_convtersToFire(player.convters)


		#for convter in player1.convters:
			#print(convter.name)
		#	print(convter.trade_for_me)

		print("start Trade time")


		TradePhase(trades)
			## PLAYERS use cubes to make new cubes
		run_convters(gamePlayers)
			#players get free planets every turn at no ship cost. 
		planet_phase(gamePlayers)










#player4.convter_cost_calc()
#run_convters([player4])
#for convter in player4.convters:
#	convter.cost_to_run()


print("start of game")
PlayTradeEmpireSimulation(1,20)


#### end of game break down? ###

#for player in gamePlayers:
#	print(player.my_name)
#	print(player.cubes.my_cubes)
#	print(sum(player.cubes.my_cubes))

print("how many trades made?")
print(tradecount)
print("fail count:")
print(tradefail_count)


duck.sound()
#player3.convters[2].cost_to_run()
#player3.convters[2].convter_output()
#print(player3.convters[2].convter_value() )

#player3.convter_cost_calc()


f = False
t = True
talk = f
if(talk == True):
	for player in gamePlayers:
		for convt in player.convters:
			print(convt.convter_name())
			print(convt.convter_value())

