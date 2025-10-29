import bge 
cont = bge.logic.getCurrentController()
from math import radians
owner = cont.owner 
scn = owner.scene
obj = scn.objects
scl = bge.logic.getSceneList()
tap = cont.sensors["tap"]

class obTreeLoc():
	seed = 0
	numObjetos = 0
	# O metodo abaixo consome muito do desempenho
	# portanto use os parametro de resto para
	# facilitar o calculo com um valor aceitavel
	def posicionarObjetos(self, numAngle, resto):
		locVar = 1
		for ob in obj:
			if "locArvore" in ob:					
				'''
				# Utilitario para gerar uma lista
				# Com os nomes dos spawners de arvores
				nomeObj = ob.name
				txtList = list(nomeObj.split("."))
				num = int(txtList[1])
				if num % 2 == 0:
					print(txtList)	
				'''	
				locVar = numAngle + 1
				numAngle = locVar
				# Para imprimir o rotulo numerico de cada
				# objeto criado apartir deste metodo:
				# print(locVar)
				'''
				As linhas abaixo sao apenas para facilitar
				a performance do game, voce pode mudar o valor
				do resto da variavel passada como argumento 
				para poder ter um melhor desempenho 
				'''

				if numAngle % resto == 0:						
					self.numObjetos += 1
					ang = ob.localOrientation.to_euler()
					grama = scn.addObject("obGramas", ob)				
					arvore = scn.addObject("obAraucaria", ob) 					
					ang.z = radians(locVar*3.725)
					#print(ang.z)
					arvore.localScale = [1.25, 1.25, 1.25]
					grama.localOrientation = ang
					grama.localScale = [0.25, 0.25, 0.25]
				else:
					ang = ob.localOrientation.to_euler()
					grama = scn.addObject("obGramas", ob)									
					ang.z = radians(locVar*7.725)
					#print(ang.z)				
					grama.localOrientation = ang
					grama.localScale = [0.2, 0.25, 0.3]
				
		print(self.numObjetos)

def addArvores():
	obTreeLoc().posicionarObjetos(0, 2)