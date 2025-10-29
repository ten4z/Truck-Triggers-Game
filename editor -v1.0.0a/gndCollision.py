import bge 
cont = bge.logic.getCurrentController()
owner = cont.owner 
scn = owner.scene
obj = scn.objects


class groundObjCollide():
    def callback_three(self, object, point, normal):
        #print('Hit by %r at %s with normal %s' % (object.name, point, normal))
        print("Colide with "+ object.name)
        '''
        if object.name == "RFD":
            obj['RFD'].applyMovement([0,0, -0.001], True)   
        elif obj['RFD'].getDistanceTo(owner) <= 0.00125:
            obj['RFD'].applyMovement([0,0,0.001], True)
        '''
        

     

    def callback_one(self, object):
        print('Hit by %r' % object.name)

    def register_callback(self, controller):
        controller.owner.collisionCallbacks.append(self.callback_three)
        controller.owner.collisionCallbacks.append(self.callback_one)

def detect():
    groundObjCollide().register_callback(cont)



