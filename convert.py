from PIL import Image
import numpy as np
import cv2
from pdf2image import convert_from_path 
import pytesseract as ocr

class Convert():
    def __init__(self):
        self.image = None
        self.text = ""
        
    def openPDF(self,pdflocale, pages=0):
        try:
            pgs = convert_from_path(pdflocale, 500)
            if pages == 0:
                self.image = pgs[0]
        except Exception as e:
            print(e)
        return self
        
    def openImage(self, imglocale):
        try:
            self.image = Image.open(imglocale)
        except Exception as e:
            print(e)
        return self
    
    def convert(self):
        try:
            img = self.image.convert('RGB')
            npimagem = np.asarray(img).astype(np.uint8)
            npimagem[:, :, 0] = 0 # zerando o canal R (RED)
            npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)
            im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)
            ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
            binimagem = Image.fromarray(thresh) 
            self.text = ocr.image_to_string(binimagem, lang='por')
            return self
        except Exception as e:
            print(e)
            return self
    
    def normalizeText(self):
        try:
            arr = self.text.split("\n")
            ret = []
            for a in arr:
                if a.strip().lstrip()!="":
                    ret.append(a)
            self.text = "\n".join(ret)
        except Exception as e:
            print(e)
        return self
    
    def getList(self):
        try:
            arr = self.text.split("\n")
            arr = [a.split(" ") for a in arr]
            return arr
        except Exception as e:
            print(e)
            return []   
    
    def getText(self):
        try:
            return self.text
        except Exception as e:
            print(e)
            return self.text
    
    def getLayout(self,layout):
        try:
            values = self.getList()
            resp = {}
            for k in layout:
                # resp[k]
                v = values
                for i in layout[k]['pos']:
                    v = v[i]
                if 'join' in layout[k]:
                    ini = layout[k]['join'][0]
                    fim = layout[k]['join'][1]
                    if fim == "F":
                        fim = len(v)
                    v = " ".join(v[ini:fim])
                resp[k] = v
            return resp
        except  Exception as e:
            print(e)
            return None