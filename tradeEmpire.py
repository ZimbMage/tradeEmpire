import random



class cubes:   # a set of player cubes 

	#brown = 0
	#white = 0 
	#green = 0 	
	#ships = 0
	#blue = 0
	#yellow = 0
	#black = 0
	#hexagon  = 0
	#vp = 0
	
	brown = 0
	white = 1
	green = 2

	blue =  3
	yellow= 4
	black = 5

	hex_ =  6

	vp =    7
	ship =  8



	# the ints above do almost nothing.


	#my_cubes = [brown,white,green,blue,yellow,black,hexagon,vp,ships]  ## well shit, this isnt self refleting. )-= 

	cubes_curentlyBeingCreated = [0] * 9


	green_name = "Green"
	white_name = "White"
	brown_name = "Brown"

	blue_name = "Blue"
	yellow_name ="Yellow"
	black_name = "Black"

	hexagon_name = "Hexagon"
	vp_name = "Points"
	ships_name = "Ships"


	cube_names = [green_name,white_name, brown_name,blue_name,yellow_name,black_name,hexagon_name,vp_name,ships_name]  ## this is good use of the stirngs above, i think. 






	#wildSmall   //// hahahah, one day..... sure... 
	#wildLarge


	def __init__(self,br,w,g,b,y,bl,h,vp,ship):  # set players start cube values. // can i do this better with a list? // yes need to update this to be a list like convters

	
		self.brown = br
		self.white = w
		self.green = g 

		self.ship = ship


		self.blue= b
		self.yellow = y
		self.black = bl


		self.hexagon  = h

		self.vp = vp

		self.my_cubes = [self.green ,self.white,self.brown,self.blue,self.yellow,self.black,self.hexagon,self.vp, self.ship]  ## well shit, this isnt self refleting. )-= 
		print(self.my_cubes)
		## i really dont need the ints above the list of ints do i. 


	def cube_Count(self):
		#print(' CubeCount:\r\n' ,self.green_name,self.green,self.white_name,self.white,self.brown_name,self.brown ,'\n\r' , self.black_name,self.black,self.yellow_name,self.yellow,self.blue_name,self.blue, '\n\r' , self.hexagon_name,self.hexagon )
		for i in range(0,len(self.my_cubes)):
			
			print(self.my_cubes[i], self.cube_names[i])

	
	def cube_convterNeeds(self,mylist):

		self.cubes_run = mylist


	def point_count(self):
		print(' Curent Score:', self.my_cubes[8])  ## really should have that 8 be some int value. 
	
	def ship_count(self):
		print(' Curent ship count:', self.my_cubes[9])  ## really should have that 9 be some int value. 


	def fixConvterShareBug(self):
		self.cubes_curentlyBeingCreated = [0] *9 ## really need to fix the bug causeing convters to load all players incoming stack



	def addcubes(self,colors,ammounts):  ### add or remove cubes. 
		#print(colors)
	#	print(self.my_cubes)
		for i in range(len(colors)):
			#print(i)
			#print(colors[i])
			#print(self.my_cubes[colors[i]])
			self.my_cubes[colors[i]] = self.my_cubes[colors[i]] + ammounts[i] 
##               cubes[colors[i]] = cubes[colors[i]] + ammounts[i]

	def update_postEcon(self):
			print('cubes to add to player below')
			print(self.cubes_curentlyBeingCreated)
			for i in range(0,len(self.cubes_curentlyBeingCreated)):
				self.my_cubes[i] = self.my_cubes[i] + self.cubes_curentlyBeingCreated[i]
			self.cubes_curentlyBeingCreated = [0] *9
			print(self.cubes_curentlyBeingCreated)
			print('clean up done')	





class convter: 
	rank = 0 # run all convters in ranked order, low to high. // will need some sort of tie breaker  
	#brown_cost = 0
	#white_cost = 0 
	#green_cost = 0 
	#blue_cost = 0
	#yellow_cost = 0
	#black_cost = 0
	
	#hexagon_cost  = 0
	
	#costs = [brown_cost,white_cost,green_cost,blue_cost,yellow_cost,black_cost,hexagon_cost]

	#blue_out = 0
	#yellow_out = 0
	#black_out = 0
	
#	brown_out = 0
#	white_out = 0 
#	green_out= 0 

#	hexagon_out = 0

#	vp_out = 0


	#outputs = [blue_out,yellow_out,black_out,brown_out,white_out,green_out,hexagon_out,vp_out]

	brown_name = "Brown"
	white_name = "White"
	green_name = "Green"

	yellow_name= "Yellow"
	blue_name =  "Blue"
	black_name = "Black"


	hexagon_name = "Hexagon"

	vp_name = "Points"
	ships_name = "Ships"

	cube_names = [green_name,white_name, brown_name,blue_name,yellow_name,black_name,hexagon_name,vp_name,ships_name]  ## this is good use of the stirngs above, i think. 







	def __init__(self,name,set_cost,set_outputs):   # need one name, 7 costs, and 8 outputs 
		self.name = name
		self.costs = [0] * 9   # the 7 and 8 will have to be increased if i add ships or wilds
		self.outputs = [0] * 9 #
		for i in range(0,len(set_cost)):
			self.costs[i] = set_cost[i]
		
		for i in range(0,len(set_outputs)):	
				self.outputs[i] = set_outputs[i]


	def convter_name(self):
		
		#print("cake")
		my_str = "Convter Name:" + self.name
		return my_str


	def cost_to_run(self):
			print(self.name, 'cost to run:')
			print(self.costs)	
			print('')



	def convter_output(self):
		print(self.name, 'outputs:')
		print(self.outputs)
		return print("")

    	

	def RunConvter(self,cubes):
		
		#print('echo')
		#print (self.convter_name())
		#print(self.convter_output())	
			#print (cake)
		#print('test')
		
		for i in range(0,len(self.costs)):
			#print('ping')
			if cubes.my_cubes[i]< self.costs[i]:
				dif = self.costs[i]-cubes.my_cubes[i]  # i see some issues
				return  print(self.name, ':missing' ,dif, self.cube_names[i] ,'cube/cubes did not run', )
				#print(self.costs)
				 

		## after looping thru
		
		#print(self.name, 'i can run now')
		for i in range(0,len(self.costs)):
			cubes.my_cubes[i] = cubes.my_cubes[i] - self.costs[i]
		for i in range (0,len(self.outputs)):
		    cubes.cubes_curentlyBeingCreated[i] = cubes.cubes_curentlyBeingCreated[i] + self.outputs[i]  ## seems like a bug in here somewhere
		#print('takeNoteBelow')
		#print(cubes.cubes_curentlyBeingCreated)

		print(self.name+ ' ran')
		return print('')		
				 





	
    	    # check that the cost can be paid
    	    #pay the cost

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





## i want a way to create a bunch of 'colonies'
## to create one, i need to create a new convter, name it, then add it to 

def random_small_Output():
		x = random.randint(0,2)
		if x == 0 :
			return [1,0,0]
		elif x == 1:
			return [0,1,0]
		else:
			return [0,0,1]    	

def add_planets (player):
		for addPlant in range (0,player.start_planet):
			addPlant = convter(("planet"+str(addPlant)),[],random_small_Output())
			player.convters.append(addPlant)
			player.planet_Count += 1
		print(str(player.planet_Count) + " " + player.my_name)
		






class player:
	def __init__(self,my_cubes,my_convters, starting_planet_count,name):   # load up all starting things 
		self.cubes = my_cubes
		self.convters = my_convters
		self.start_planet = starting_planet_count 
		self.planet_Count = 0
		self.my_name = name

## need to write a function that figures out what cubes i will not use with my curent convters. -> create a list of all convter costs. 
	def convter_cost_calc(self):
		print(self.my_name + " curent convter needs")
		self.upcomeingCosts = [0]*9
		for convter in self.convters:
			for i in range(0,len(convter.costs)):
				self.upcomeingCosts[i] = self.upcomeingCosts[i] + convter.costs[i]
		for i in range(0,len(self.upcomeingCosts)):
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
		






#self,brown,w,green,blue,y,black,h,ship)
p1cubes = cubes(2,1,1,1,2,2,0,0,4)   # red
p2cubes = cubes(3,2,3,1,1,1,1,0,0)   # brown 
p3cubes = cubes(2,4,5,0,0,2,0,0,1) #green
p4cubes = cubes(1,3,0,1,1,0,1,0,1) #yellow 

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

player1 = player(p1cubes,convters,2,"KJASJAVIKALMM (two fleet bid ppl)") ## thats much more clear then "bob"
player2 = player(p2cubes,p2convters,1,"KT'ZR'TY'RTL (BUG ppl)")
player3 = player(p3cubes,p3convters,2,"Caylion")
player4 = player(p4cubes,p4convters,1,"Faderan")

#convters.append()
print("add planets")

add_planets(player1) ## add x random small planets
add_planets(player2)
add_planets(player3)
add_planets(player4)

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



red1 = convter("red1",[],[0,0,2,0,0,0,0,0,3])
player1.convters.append(red1)
#red1.convter_output()

red2 = convter("red2",[0,0,0,2,0,0,0,0,0],[1,0,0,0,0,0,0,0,4])
player1.convters.append(red2)

red3 = convter("red3",[0,0,4,0,0,0,0,0,0],[0,1,0,1,1,1,0,0,0])
player1.convters.append(red3)

brown1 = convter("brown1",[],[0,0,0,0,0,0,1,0,1])
player2.convters.append(brown1)

brown2 = convter("brown2",[5,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,0,0,4])
player2.convters.append(brown2)

brown3 = convter("brown3",[0,0,0,0,0,0,1,0,0],[1,1,2,0,0,0,0,0,0])
player2.convters.append(brown3)


green1 = convter("green1",[],[sum(x) for x in zip(green,green,green,white,ships)]) # not awful! 
player3.convters.append(green1)

green2 = convter("green2",[0,0,0,2,0,0,0,0,0],[0,1,0,0,0,1,0,0,2])
player3.convters.append(green2)

green3 = convter("green3",[2,0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0])
player3.convters.append(green3)

green4 = convter("green4",[0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0])
player3.convters.append(green4)


yellow1 = convter("yellow1",[0,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,1])
player4.convters.append(yellow1)

yellow2 = convter("yellow2",[0,4,0,0,0,0,0,0,0],[1,0,0,0,0,1,1,0,0])
player4.convters.append(yellow2)

yellow3 = convter("yellow3",[0,0,2,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,2])
player4.convters.append(yellow3)

yellow4 = convter("yellow4",[3,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,0])
player4.convters.append(yellow4)


#print(player1.convters)





#### run all convters

# self.convters = my_convters
#self.cubes = my_cubes
#self.convters = my_convters
#self.start_planet = starting_planet_count 
#self.planet_Count = 0
#self.my_name = name

gamePlayers = [player1,player2,player3,player4]



def run_convters(players):
		for player in players:

			print('******* running convters for ' + player.my_name  + ' *******')
			#print('test something(player cubes)')
			#print(player.cubes)
			#print("clean convter share bug")
			
			player.cubes.fixConvterShareBug()

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

	
	print("start pf trade")
	print("####################################")

	print(player_offer.my_name)
	print("what do i have?")
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





	## this is a trade in action....
	if index_of_cube_i_want != -99 and index_of_their_cube !=-99:
		## we can and will trade 1 for 1. 
		# i lose and gain one cube.
		#print(player_offer.cubes.cube_Count())
		player_offer.cubes.addcubes([index_of_cube_i_want,index_of_their_cube], [1,-1])
		Player_reciveingOffer.cubes.addcubes([index_of_cube_i_want,index_of_their_cube], [-1,1])
		#print("Post swap")
		#print(player_offer.cubes.cube_Count())
		player_offer.convter_cost_calc_silent()
		Player_reciveingOffer.convter_cost_calc_silent()
		print("trade happned")
		tradecount = tradecount +1 
	else :
		print("no trade")
		tradefail_count = tradefail_count + 1 
	print("End of trade")
	print("####################################")






    








### need a trade phase
# how many trades should i try to do? lets start with 50

print ( " Start of Trade Phase")

for player in gamePlayers:
	player.convter_cost_calc()

#player1.convter_cost_calc()

for unused in range(100):
	trade_pair = random.sample(gamePlayers,2)
	trade_offer(trade_pair[0],trade_pair[1])


print("trades")
print(tradecount)

print("trades done, post trade info")
for player in gamePlayers:
	player.convter_cost_calc()

####need to offer trades
## bob knows what cubes he needs, knows what extra cubes he has. bob can offer cubes at random for what alice has or offer something alice needs.  

## 

##### for now, always say yes. no real rejection logic. 


### econ phase
#run_convters(gamePlayers)


### add planet phase

