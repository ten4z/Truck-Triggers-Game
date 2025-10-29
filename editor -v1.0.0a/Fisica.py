import bge
from math import radians
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects
scl = bge.logic.getSceneList()

keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
KEY_ACTIVE = bge.logic.KX_INPUT_ACTIVE

gdict = bge.logic.globalDict
mudar_claridade = cont.actuators["mudar_claridade"]  

class Truck():
	def __init__(self):
		if own['ligar_farois'] == True:
			obj['farol_spot_1'].visible = True
			obj['farol_spot_2'].visible = True
		else:
			obj['farol_spot_1'].visible = False
			obj['farol_spot_2'].visible = False
		if own['agora_eh_dia'] == True:
			obj['sol'].energy = 500.0
			obj['luz_ambiente'].energy = 1.25
		else:
			obj['sol'].energy = 0.25
			obj['luz_ambiente'].energy = 0.1


	def addSkyDome(self):
		if addSky.positive:
			cont.activate(activateSky)

	def dictCamOri(self):
		eixo = obj["eixo_look"]
		camOri = eixo.localOrientation.to_euler() 
		gdict['camOri'] = camOri

	def ligar_desligar_farois(self):
		if keyboard.events[bge.events.F2KEY] == JUST_ACTIVATED:  
			cont.activate(cont.actuators['toggle_farois'])
			if own['ligar_farois'] == True:
				obj['farol_spot_1'].visible = True
				obj['farol_spot_2'].visible = True
			else:
				obj['farol_spot_1'].visible = False
				obj['farol_spot_2'].visible = False
		
			

	def eixos_posicao(self):		
		if cont.sensors['tap'].positive:
			obj['RFD'].localPosition.x = obj['chassi'].localPosition.x + 0.65
			obj['RFD'].localPosition.y = obj['chassi'].localPosition.y + 0.7
			obj['RFD'].localPosition.z = obj['chassi'].localPosition.z 
			obj['RFE'].localPosition.x = obj['chassi'].localPosition.x - 0.65
			obj['RFE'].localPosition.y = obj['chassi'].localPosition.y + 0.7
			obj['RFE'].localPosition.z = obj['chassi'].localPosition.z                         
			obj['RTD'].localPosition.x = obj['chassi'].localPosition.x + 0.65
			obj['RTD'].localPosition.y = obj['chassi'].localPosition.y - 0.65
			obj['RTD'].localPosition.z = obj['chassi'].localPosition.z
			obj['RTE'].localPosition.x = obj['chassi'].localPosition.x - 0.65
			obj['RTE'].localPosition.y = obj['chassi'].localPosition.y - 0.65
			obj['RTE'].localPosition.z = obj['chassi'].localPosition.z					
			obj['RTD2'].localPosition.x = obj['chassi'].localPosition.x + 0.65
			obj['RTD2'].localPosition.y = obj['chassi'].localPosition.y - 1.35
			obj['RTD2'].localPosition.z = obj['chassi'].localPosition.z
			obj['RTE2'].localPosition.x = obj['chassi'].localPosition.x - 0.65
			obj['RTE2'].localPosition.y = obj['chassi'].localPosition.y - 1.35
			obj['RTE2'].localPosition.z = obj['chassi'].localPosition.z

	def reposicionar_truck_vertical(self):
		if keyboard.events[bge.events.F5KEY] == JUST_ACTIVATED:            
			eixo_normal = [0, 0, 0]        
			obj['fisica_truck'].localOrientation= eixo_normal
			obj['fisica_truck'].localPosition.z =  obj['fisica_truck'].localPosition.z + 1.5            
			self.eixos_posicao()
			
	def engine(self):        
		obj['loc_truck'].localOrientation = obj['fisica_truck'].localOrientation
		obj['loc_truck'].localPosition.x = obj['fisica_truck'].localPosition.x
		obj['loc_truck'].localPosition.y = obj['fisica_truck'].localPosition.y
		obj['loc_truck'].localPosition.z = obj['fisica_truck'].localPosition.z + 0.25
		
		if cont.sensors['col_gd_rtd'].positive:
			obj['RTD'].applyMovement([0,0, -0.01], True)
		elif obj['RTD'].getDistanceTo(obj['chassi']) < 1.05:
			obj['RTD'].applyMovement([0,0,0.01], True)  
		
		if cont.sensors['col_gd_rte'].positive:
			obj['RTE'].applyMovement([0,0, -0.01], True)
		elif obj['RTE'].getDistanceTo(obj['chassi']) <= 1.05:
			obj['RTE'].applyMovement([0,0,0.01], True)  
					
		if cont.sensors['col_gd_rtd2'].positive:
			obj['RTD2'].applyMovement([0,0, -0.01], True)
		elif obj['RTD2'].getDistanceTo(obj['chassi']) <= 1.55:
			obj['RTD2'].applyMovement([0,0,0.01], True)  			
		
		if cont.sensors['col_gd_rte2'].positive:
			obj['RTE2'].applyMovement([0,0, -0.01], True)
		elif obj['RTE2'].getDistanceTo(obj['chassi']) <= 1.55:
			obj['RTE2'].applyMovement([0,0,0.01], True)  
			
		if cont.sensors['col_gd_rfe'].positive:
			obj['RFE'].applyMovement([0,0,-0.01], True)
		elif obj['RFE'].getDistanceTo(obj['chassi']) <= 1.05:
			obj['RFE'].applyMovement([0,0,0.01], True)  

		if cont.sensors['col_gd_rfd'].positive:
			obj['RFD'].applyMovement([0,0, -0.01], True)   
		elif obj['RFD'].getDistanceTo(obj['chassi']) <= 1.05:
			obj['RFD'].applyMovement([0,0,0.01], True)        

	def engine_de_orientacao(self):        
		u1 = obj['RFE'].localPosition
		v1 = obj['RFD'].localPosition
		
		u2 = obj['RTE'].localPosition
		v2 = obj['RTD'].localPosition
		
		u3 = obj['dir'].localPosition
		v3 = obj['mid'].localPosition   		

		u4 = obj['RTE2'].localPosition
		v4 = obj['RTD2'].localPosition

		direcao1 = u1 - v1
		obj['dir'].localPosition = (u1 + v1)/2
		obj['dir'].localScale = [direcao1.length/2, 0.05, 0.05]                   
		#obj['dir'].alignAxisToVect(direcao1, 0)
		obj['dir'].localOrientation = direcao1
					 
		direcao2 = u2 - v2
		obj['mid'].localPosition = (u2 + v2)/2
		obj['mid'].localScale = [direcao2.length/2, 0.05, 0.05]
		obj['mid'].localOrientation = direcao2
		
		direcao3 = u3 - v3
		obj['eixo'].localPosition = (u3 + v3)/2
		obj['eixo'].localScale = [0.05, direcao3.length/2,0.05]
		obj['eixo'].localOrientation = direcao3

		direcao4 = u4 - v4
		obj['eixo2'].localPosition = (u4 + v4)/2
		obj['eixo2'].localScale = [direcao4.length/2,0.05, 0.05]
		obj['eixo2'].localOrientation = direcao4

		obj['eixo_a'].localPosition = obj['dir'].localPosition
		obj['eixo_a'].localOrientation = direcao1
		obj['eixo_b'].localPosition = obj['mid'].localPosition
		obj['eixo_b'].localOrientation = direcao2
		obj['eixo_c'].localPosition = obj['eixo2'].localPosition
		obj['eixo_c'].localOrientation = direcao4


	def direcao(self):
		vl_ang = [0, 0, 0]
		if obj['RFD']['angulo'] == obj['RFE']['angulo']:
			if obj['RFD']['angulo'] >= 100:
				obj['RFD']['angulo'] = 100 
				obj['RFE']['angulo'] = 100
			elif obj['RFD']['angulo'] <= 0:
				obj['RFD']['angulo'] = 0
				obj['RFE']['angulo'] = 0
		else:
			obj['PFD']['angulo'] = obj['PFE']['angulo']
		
		if keyboard.events[bge.events.SKEY] == KEY_ACTIVE:
			self.re_truck()
			if cont.sensors['girar_direita'].positive:
				obj['RFE']['angulo'] -= 2
				obj['RFD']['angulo'] -= 2
				if cont.sensors['col_gd_rtd'].positive or cont.sensors['col_gd_rte'].positive or cont.sensors['col_gd_rtd2'].positive or cont.sensors['col_gd_rte2'].positive:
					vl_ang[2] -= 0.5          
					obj['fisica_truck'].setAngularVelocity(vl_ang, True)                                
			elif cont.sensors['girar_esquerda'].positive:
				obj['RFD']['angulo'] += 2
				obj['RFE']['angulo'] += 2          
				if cont.sensors['col_gd_rtd'].positive or cont.sensors['col_gd_rte'].positive or cont.sensors['col_gd_rtd2'].positive or cont.sensors['col_gd_rte2'].positive:   
					vl_ang[2] += 0.5      
					obj['fisica_truck'].setAngularVelocity(vl_ang, True)
			else:
				obj['RFE']['angulo'] = 50
				obj['RFD']['angulo'] = 50            
		else:
			if cont.sensors['girar_direita'].positive:
				obj['RFD']['angulo'] += 2
				obj['RFE']['angulo'] += 2
				if cont.sensors['col_gd_rtd'].positive or cont.sensors['col_gd_rte'].positive or cont.sensors['col_gd_rtd2'].positive or cont.sensors['col_gd_rte2'].positive:
					vl_ang[2] -= 0.5                    
					obj['fisica_truck'].setAngularVelocity(vl_ang, True)                				
			elif cont.sensors['girar_esquerda'].positive:
				obj['RFE']['angulo'] -= 2
				obj['RFD']['angulo'] -= 2
				if cont.sensors['col_gd_rtd'].positive or cont.sensors['col_gd_rte'].positive or cont.sensors['col_gd_rtd2'].positive or cont.sensors['col_gd_rte2'].positive:
					vl_ang[2] += 0.5           
					obj['fisica_truck'].setAngularVelocity(vl_ang, True)
			else:
				obj['RFE']['angulo'] = 50
				obj['RFD']['angulo'] = 50

		cont.activate(cont.actuators['direcao_rfd'])
		cont.activate(cont.actuators['direcao_rfe'])
		
	def re_truck(self):
		if  keyboard.events[bge.events.SKEY] == KEY_ACTIVE:
			if cont.sensors['col_gd_rtd'].positive or cont.sensors['col_gd_rte'].positive or cont.sensors['col_gd_rtd2'].positive or cont.sensors['col_gd_rte2'].positive:
				obj['fisica_truck'].applyForce([0,-1.25,0], True)	


	def acelerar_truck(self):		
		if  keyboard.events[bge.events.WKEY] == KEY_ACTIVE:
			if cont.sensors['col_gd_rtd'].positive or cont.sensors['col_gd_rte'].positive or cont.sensors['col_gd_rtd2'].positive or cont.sensors['col_gd_rte2'].positive:
				obj['fisica_truck'].applyForce([0, 4.5, 0], True)

	def atualizar_minimapa(self):  
		pose_x = obj['loc_truck'].localPosition.x 
		pose_y = obj['loc_truck'].localPosition.y            
		gdict['px'] = pose_x
		gdict['py'] = pose_y
		xyz = obj['fisica_truck'].localOrientation.to_euler()          
		gdict['rot'] = [0, 0, xyz.z]
		vl = obj['fisica_truck'].getLinearVelocity().length

		gdict['velocidade'] = int(vl * 1.75)

	def mudar_camera(self):
		if keyboard.events[bge.events.VKEY] == JUST_ACTIVATED:
			obj['logica_truck']['camera'] += 1  
			if obj['logica_truck']['camera'] == 1:
				scn.active_camera = obj["camera_longe"]
			elif obj['logica_truck']['camera'] == 2:				
				scn.active_camera = obj["camera_truck"]				
			elif obj['logica_truck']['camera'] == 3:
				scn.active_camera = obj["camera_top"]	
			else:
				obj['logica_truck']['camera'] = 1
				scn.active_camera = obj["camera_look"]
	def alternar_dia_noite(self):
		if keyboard.events[bge.events.F3KEY] == JUST_ACTIVATED:
			cont.activate(mudar_claridade)
		if own['agora_eh_dia'] == True:
			obj['sol'].energy = 50.0
			obj['luz_ambiente'].energy = 1.0
		else:
			obj['sol'].energy = 5.0
			obj['luz_ambiente'].energy = 0.05

	def camera_top(self):
		# posição do sol   
		obj['loc_sol'].localPosition = obj['fisica_truck'].localPosition        
		# localização inicial do truck

		obj['eixo_look'].localPosition.x = obj['fisica_truck'].localPosition.x
		obj['eixo_look'].localPosition.y = obj['fisica_truck'].localPosition.y
		obj['eixo_look'].localPosition.z = obj['fisica_truck'].localPosition.z
		
	def alternar_visibilidade_do_truck(self):
		if JUST_ACTIVATED in keyboard.inputs[bge.events.F9KEY].queue:
			if obj['chassi'].visible == True:
				obj['chassi'].visible = False
			else:
				obj['chassi'].visible = True
 
def Motor_do_Truck():

	Truck().dictCamOri()
	Truck().eixos_posicao()
	Truck().engine_de_orientacao()
	Truck().engine()
	Truck().direcao()
	Truck().acelerar_truck()
	Truck().reposicionar_truck_vertical()
	Truck().ligar_desligar_farois()
	Truck().re_truck()
	Truck().camera_top()
	Truck().alternar_visibilidade_do_truck()
	Truck().atualizar_minimapa()
	Truck().mudar_camera()
	Truck().alternar_dia_noite()