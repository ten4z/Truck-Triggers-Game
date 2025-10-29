
#import GameLogic
import GameLogic

scene = GameLogic.getCurrentScene()
controller = GameLogic.getCurrentController()

obj = scene.objects
objeto = controller.owner
scl = GameLogic.getSceneList()
truck = obj['fisica_truck']


cam_direita = obj["cam_vd_direito"]	
cam_esquerda = obj["cam_vd_esquerdo"]

class DynamicGlass():
	def fun(self):
		for sc in scl:
			if sc.name == "inicio":
				cam_direita.visible = False
				cam_esquerda.visible = False

		if "RenderToTexture_Direito" and "RenderToTexture_Esquerda"  in objeto:				
			objeto["RenderToTexture_Direito"].refresh(True)
			objeto["RenderToTexture_Esquerda"].refresh(True)
		else:
			import VideoTexture				
			cam_direita.visible = True
			cam_direita.lens = 10
			ID_mat_direito = VideoTexture.materialID(objeto, "MA" + objeto['material_direito'])
			renderToTexture = VideoTexture.Texture(objeto, ID_mat_direito)
			renderToTexture.source = VideoTexture.ImageRender(scene, cam_direita)
			objeto["RenderToTexture_Direito"] = renderToTexture								
			cam_esquerda.visible = True		
			cam_esquerda.lens = 10
			ID_mat_esquerdo = VideoTexture.materialID(objeto, "MA" + objeto['material_esquerdo'])
			renderToTexture = VideoTexture.Texture(objeto, ID_mat_esquerdo)
			renderToTexture.source = VideoTexture.ImageRender(scene, cam_esquerda)
			objeto["RenderToTexture_Esquerda"] = renderToTexture		
		
def EspRetro(self):
	DynamicGlass().fun()
