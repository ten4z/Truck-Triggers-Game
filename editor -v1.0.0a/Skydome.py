import bge
import time
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene 
obj = scn.objects 

ceu = obj["malhaFirmamento"]
gdict = bge.logic.globalDict

class Firmamento():
	def atualizarOCeu(self):		


		obj['axisSky'].localOrientation = gdict['camOri']
		
		if own["tmpTextura"] >= 0:
			pass

			


		if own["tmpTextura"] >= 0.9:
			own["numTextura"] += 1
			
			ceu.replaceMesh("f" + str(own["numTextura"]))
			
			own["tmpTextura"] = 0
		if own["numTextura"] < 0 or own["numTextura"] >= 5:
			own["numTextura"] = 0
		

def Show():
	Firmamento().atualizarOCeu()


