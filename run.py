import cv2 
import os 
import numpy as np 
from skimage.feature import graycomatrix, graycoprops




def indexer_images_grayscale(chemin_repertoire): 
    index = {} 
    for nom_fichier in os.listdir(chemin_repertoire): 
        chemin_fichier = os.path.join(chemin_repertoire, nom_fichier) 
        if chemin_fichier.lower().endswith(('.png', '.jpg', '.jpeg')): 
            image = cv2.imread(chemin_fichier, cv2.IMREAD_GRAYSCALE)  
            histogramme = cv2.calcHist([image], [0], None, [256], [0, 256])  
            index[nom_fichier] = histogramme.flatten() 
    return index 


def rechercher_images_similaires_grayscale(index, histogramme_requete, nombre_resultats=5): 
    distances = [] 
    for nom_fichier, histogramme_indexe in index.items(): 
        distance = np.linalg.norm(histogramme_requete - histogramme_indexe)  
        distances.append((nom_fichier, distance)) 
    distances.sort(key=lambda x: x[1]) 
    return distances[:nombre_resultats] 


chemin_repertoire = "Apple Red 1"  
index_images_grayscale = indexer_images_grayscale(chemin_repertoire)

chemin_image_requete = "r_4_100.jpg" 
image_requete = cv2.imread(chemin_image_requete, cv2.IMREAD_GRAYSCALE)  
histogramme_requete = cv2.calcHist([image_requete], [0], None, [256], [0, 256]).flatten()  

resultats = rechercher_images_similaires_grayscale(index_images_grayscale, histogramme_requete)
print(resultats)