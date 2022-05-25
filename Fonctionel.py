import cv2
import time
import base64
from PIL import Image
import csv
import logging

#Ouverture de la caméra avec OpenCV
cap = cv2.VideoCapture(0)
i = 0

#Input demandant le nombre de frames à l'utilisateur
n = int(input("Combien de frames ? "))

def framing(n):
    #Boucle jusqu'au nombre de frames demandé 
    for i in range (n):
        time.sleep(1)
        #ret est un booléen permettant de savoir si la caméra est toujours allumée.
        #frame récupère une frame capturé de la caméra.
        ret, frame = cap.read()

        #On break pour éviter la boucle infinie
        if ret == False:
            break

        #On enregistre la frame dans un dossier.
        cv2.imwrite('Frame'+str(i)+'.jpg', frame)

        img_file = Image.open('/home/user/Frames/''Frame'+str(i)+'.jpg')

        #Fonction permettant de compresser l'image pour éviter un encodage très long.
        resized = img_file.resize((150,150),Image.ANTIALIAS)
        resized.save('/home/user/Frames/Resized/image_scaled'+str(i)+'.jpg',quality=95)

        #Lecture de l'image compressée permettant de l'encoder par la suite.
        with open('/home/user/Frames/Resized/image_scaled'+str(i)+'.jpg', "rb") as image:
            my_string = base64.b64encode(image.read())
        
        #Initialisation pour le format de notre log.
        Log_Format = "%(message)s"
        
        #Configuration du "log", nom, mode d'écriture.
        logging.basicConfig(filename = "logfile.log",
                                filemode = "w",
                                format = Log_Format)
        logger = logging.getLogger()
        #Le message du log sera en fait notre encodage B64 de notre image.
        #On rajoute l'entete B64 avant pour pouvoir display l'image dans notre dashboard Grafana.
        logger.error('data:image/jpeg;base64,' + my_string.decode('utf-8'))
        print('Frame ' + str(i) + ' enregistrée')
            
        i += 1
    
    #Des que la dernière frame est atteinte, on éteint la caméra.
    cap.release()
    cv2.destroyAllWindows()

#Appel de la fonction.
framing(n)
