

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


pass			