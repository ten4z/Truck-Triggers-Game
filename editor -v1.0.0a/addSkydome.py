import bge
import time
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene 
obj = scn.objects 


addSky = cont.sensors["addSky"]
activateSky = cont.actuators["activateSky"]

class adicionarFirmamento():
	def addSky(self):		
		
		cont.activate(activateSky)
	
	
		

def Add():
	adicionarFirmamento().addSky()


