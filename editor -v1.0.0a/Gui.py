import bge
cont = bge.logic.getCurrentController()
own = cont.owner
scn = own.scene
obj = scn.objects

gdict = bge.logic.globalDict
sp = cont.actuators['set_ponteiro']
pv = cont.actuators['ponteiro_velocidade']

class Gui():
    def indicador_de_velocidade(self):
        obj['txt_velocidade'].resolution = 5   
        v =  int(gdict['velocidade'])
        obj['ponteiro']['velocidade'] = v
        obj['txt_velocidade']['Text'] = str(v) + " km/h"
        sp.value = str(v)
        cont.activate(sp)        
        cont.activate(pv)    
 
def panel():
    Gui().indicador_de_velocidade()