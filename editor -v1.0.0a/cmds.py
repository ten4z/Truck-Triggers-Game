import bge
from math import radians
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
scl = bge.logic.getSceneList()
tap = cont.sensors["tap"]

keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
KEY_ACTIVE = bge.logic.KX_INPUT_ACTIVE

toggle_hud = cont.actuators["toggle_hud"]
'''
setCam = cont.actuators["setCam"]
addGui = cont.actuators["addGui"]
'''
#print(scl.scenes["inicio"]["Launcer"]["value"])

class Entrada():
	def __init__(self):		
		if tap.positive:			
			pass

	def compareHudGui(self):

		if  keyboard.events[bge.events.F10KEY] == JUST_ACTIVATED:
			cont.activate(toggle_hud)			

			if own["pausarGui"]:						
				for sc in scl:				
					if sc.name in ["gui", "hud_engine", "hud_view"]:
						print(sc.name)												
						sc.suspend()						
						own['espObj'] = False				
			else:				
				for sc in scl:
					if sc.name in ["gui", "hud_engine", "hud_view"]:
						sc.resume()
						own['espObj'] = True
			
	def pausarHudGui(self):
		self.compareHudGui()
		
	def comandoDeInterface(self):
		self.pausarHudGui()
			
def EntSaida():
	Entrada().comandoDeInterface()