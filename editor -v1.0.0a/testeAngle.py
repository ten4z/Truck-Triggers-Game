

obj = ["locArvore", "locArvore", "locArvore", "locArvore"]

class Angle():
    
    def determinarAngle(self, numAngle):
        locVar = 1
        for ob in obj:
            if "locArvore" in ob:
                locVar = numAngle + 1
                numAngle = locVar
                print(locVar)
                #print(int(numAngle)*100)


if __name__ == "__main__":
    Angle().determinarAngle(0)
                
