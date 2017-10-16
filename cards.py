import cubes


class convter: 
	rank = 0 # run all convters in ranked order, low to high. // will need some sort of tie breaker  
	#brown_cost = 0 
	#white_cost = 0 
	#green_cost = 0 

	#blue_cost = 0
	#yellow_cost = 0
	#black_cost = 0
	
	#hexagon_cost  = 0
	

	#blue_out = 0
	#yellow_out = 0
	#black_out = 0
	
#	brown_out = 0
#	white_out = 0 
#	green_out= 0 

#	hexagon_out = 0

#	vp_out = 0


	
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







	def __init__(self,name,set_cost,set_outputs,card_type):   # need one name, 7 costs, and 8 outputs 
		self.name = name
		self.costs = [0] * 9   # 9 will have to be increased if i add wilds?
		self.outputs = [0] * 9 #
		self.convter_type = card_type
		self.trade_for_me = False


		for i in range(len(set_cost)):
			self.costs[i] = set_cost[i]
		
		for i in range(len(set_outputs)):	
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

	def convter_value(self):   # retun value of convter after subtracting value required to run. 
		value_in = 0
		value_out = 0
		for i in range(len(self.costs)) :
			if i < 3:
				value_in = value_in + self.costs[i]
			#	print (" i is = " + str(i))
				#print(self.costs[i])
				#print("value_in")
				#print(value_in)
			elif i > 2 and i < 6:
				value_in = value_in + (self.costs[i]*1.5)	
			#	print(value_in)
			elif i ==6 or i ==7:
				value_in = value_in + (self.costs[i]*3)	
			#	print(value_in)
			else:
				value_in = value_in + (self.costs[i])	
			#	print(value_in)
		

		for i in range(len(self.outputs)):
			if i < 3:
				value_out = value_out + self.outputs[i]
			elif i > 2 and i < 6:
				value_out = value_out + (self.outputs[i]*1.5)	
			elif i ==6 or i ==7:
				value_out = value_out + (self.outputs[i]*3)	
			else:
				value_out = value_out + (self.outputs[i])	
		#print(value_in)
		#print(value_out)
		#print("")
		return((value_out)-(value_in))









	def RunConvter(self,cubes):
		
		#print('echo')
		#print (self.convter_name())
		#print(self.convter_output())	
			#print (cake)
		#print('test')
		
		for i in range(len(self.costs)):
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
		return print('')	# returing blank string becuse before was geting strange spam	
				 





	

pass