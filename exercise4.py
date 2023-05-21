import cv2
from pyzbar.pyzbar import decode
from barcode import EAN13

codigo = ""

def reader(image):
    img = cv2.imread(image)
    img = cv2.resize(img, (523, 280))
    
    detectedBarcodes = decode(img)

    if not detectedBarcodes:
        print("Código de barras no detectado")
    else:

        for barcode in detectedBarcodes:
            (x,y,an,al) = barcode.rect
            cv2.rectangle(img, (x-10, y-10),
                          (x + an+10, y + al+10),
                          (255,0,0), 2)
            
            if barcode.data!="":

                codigo = barcode.data.decode()
                codigo = codigo[:-1]
                print(codigo.__class__)
                print(f"ID ALUMNO: {codigo}")


    cv2.imshow("Código", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image = "/home/chema/Documentos/CFGS-DAM/COMPUTER SYSTEMS/THIRD TERM/THIRD-TERM-ASSESABLE-ACTIVITY/Alumno 01.png"
    reader(image)
