import bge
import time
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene 
obj = scn.objects 
tap = cont.sensors["tap"]

keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
KEY_ACTIVE = bge.logic.KX_INPUT_ACTIVE
numTruck = cont.actuators["numTruck"]

class selecionarTruck():
	def escolha(self):
		if own["truck"] <= 0:		
			own["truck"] = 6
		elif own["truck"] > 6:
			own["truck"] = 1
		if keyboard.events[bge.events.F6KEY] == JUST_ACTIVATED:
			own["truck"] += 1
			
		self.determinarTruck()

	def determinarTruck(self):
	
		if own["truck"] == 1:
			obj["chassi"].replaceMesh("chassi")
		elif own["truck"] == 2:
			obj["chassi"].replaceMesh("truck2")
		elif own["truck"] == 3:
			obj["chassi"].replaceMesh("truck3")
		elif own["truck"] == 4:
			obj["chassi"].replaceMesh("truck4")
		elif own["truck"] == 5:
			obj["chassi"].replaceMesh("truck5")
		elif own["truck"] == 6:
			obj["chassi"].replaceMesh("truck6")

	
		

def selecione():
	selecionarTruck().escolha()


