import GameLogic
scene = GameLogic.getCurrentScene()
controller = GameLogic.getCurrentController()
obj = controller.owner
scl = GameLogic.getSceneList()
gdict = GameLogic.globalDict

def myMap():
	for sc in scl:
		if sc.name == "hud_engine":
			# 8 * px / 360
			px = float(gdict['px'])/45
			py = float(gdict['py'])/45
			
			sc.objects['eixo_hud'].localPosition = [px, py, 0]
			sc.objects['cursor_hud'].localOrientation = gdict['rot']
	
	if "RenderToTexture" in obj:
		obj["RenderToTexture"].refresh(True)
	
	else:		
		import VideoTexture
		for sc in scl:
			if sc.name == "hud_engine":
				
				objList = sc.objects
				camName = 'cam_hud'
				cam = objList[camName]
				matID = VideoTexture.materialID(obj, "MA" + obj['material'])				
				renderToTexture = VideoTexture.Texture(obj, matID)
				renderToTexture.source = VideoTexture.ImageRender(sc,cam)
				obj["RenderToTexture"] = renderToTexture
				