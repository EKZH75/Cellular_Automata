__author__ = 'ekravitzch'


import pygame
import copy
from pygame.locals import *
import random

pygame.init() #demarrer pygame
print("hello word")

fenetre = pygame.display.set_mode((1600, 1100), RESIZABLE) #resizable ne marche pas
pygame.time.Clock().tick(30)


##################### donnees generales du systeme ##############################

green = (0,255,0)  ######### couleur des cellules
Mat_AC =[]          ####### le plateau general de l automate
Cote = 10           ######
TailleCotePixel = 15 #en pixels
coga= (300,10)      ## coordonnees du coin en haut a gauche
#ligne=Cote*[0]
#print(ligne)

 #####on construit la matrice ####
for k in range(Cote):
    Mat_AC.append(Cote*[0])


def extractCellViv(matrice):
    CellViv =[]
    for l in range(len(matrice)):
        for c in range(len(l)):
            return




for k in range (Cote+1): #on trace les contours de lautomate
    pygame.draw.line(fenetre, green, (coga[0], coga[1]+k*TailleCotePixel), (coga[0]+Cote*TailleCotePixel, coga[1]+k*TailleCotePixel), 1)
    pygame.draw.line(fenetre, green ,(coga[0]+k*TailleCotePixel, coga[1]),(coga[0]+k*TailleCotePixel, coga[1]+Cote*TailleCotePixel) ,1 )
pygame.display.flip()

#pygame.draw.rect(fenetre,green ,(500, 500,10,10) ) dessine un rectangle sur le coin 500:500 de cotes 10*10
pygame.display.flip()

def getClick(eventt):
    if eventt.type == MOUSEBUTTONDOWN and eventt.button ==1:
        return eventt.pos
    else:
        return None

def PixelHaGa(coordoonees): # renvoie le pixel en Ha a Ga pde la case dans laquelle la coordonnee se trouve

    buffer =[coordoonees[0] -coga[0],coordoonees[1] -coga[1]]

    reste_x =buffer[0]%TailleCotePixel
    reste_y =buffer[1]%TailleCotePixel

    return(coordoonees[0]-reste_x,coordoonees[1]-reste_y )

def CaseMat(PixelHaGa_):    #renvoie la case associe au pixel en haut a gauche
    buffer = [(PixelHaGa_[0] -coga[0])/TailleCotePixel,(PixelHaGa_[1]-coga[1])/TailleCotePixel]
    #buffer = [(PixelHaGa_[0] )/TailleCotePixel,(PixelHaGa_[1])/TailleCotePixel]

    return [int(buffer[0]), int(buffer[1])]

def afficheMat(Mat):
    for elt in Mat:
        print(elt)
    return


def RegleLoc(l,c,Matrice_):
    cellules_viv= 0
    liste0= [(l-1,c-1), (l-1,c), (l-1,c+1),     (l,c-1), (l,c+1),      (l+1,c-1),(l+1,c),(l+1,c+1)]
    liste =[]

    for elt in liste0:#on verifie que le voisin est bien dans l espace de def

        if elt[0]>= 0 and elt[0]<len(Matrice_) and elt[1]>= 0 and elt[1]<len(Matrice_):
            liste.append(elt)

    for elt in liste:#on compte les cell vivantes
        if Matrice_[elt[0]][elt[1]] == 1:
            cellules_viv +=1

    if Matrice_[l][c]==1: #si la cell est vivante
        #pygame.draw.line(fenetre, (255,0,0), (coga[0]+l*TailleCotePixel,coga[1]+c*TailleCotePixel),(coga[0]+(l+1)*TailleCotePixel,coga[1]+(c+1)*TailleCotePixel ))
        pygame.display.flip()
        """for elt in liste:
            pygame.draw.line(fenetre, (0,50,5), (coga[0]+elt[0]*TailleCotePixel,coga[1]+elt[1]*TailleCotePixel),(coga[0]+(elt[0]+1)*TailleCotePixel,coga[1]+(elt[1]+1)*TailleCotePixel ))
            pygame.display.flip()
        continuertampon =1
        while continuertampon:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE :            #on avance d un
                    continuertampon =0"""

        #ca cest les voisins
        #pygame.draw.line(fenetre, green, (coga[0], coga[1]+k*TailleCotePixel), (coga[0]+Cote*TailleCotePixel, coga[1]+k*TailleCotePixel), 1)
        #pygame.draw.rect(fenetre, green, (coga[0]+ l*TailleCotePixel +1, coga[1]+ c*TailleCotePixel  +1 ,TailleCotePixel-1, TailleCotePixel-1))
        if cellules_viv==2 or cellules_viv==3:
            return 1
        else:
            return 0
    if Matrice_[l][c]==0: #si la cell est morte
        if cellules_viv ==3:
            return 1
        else:
            return 0


def randomMat():
    Matrand = []
    for k in range(Cote):
        Matrand.append([])
        for l in range(Cote):
            val = random.randint(0,1)
            Matrand[k].append(val)

    return Matrand

def reinitialise(Mat):
    NouvMat = copy.deepcopy(Mat)

    for l  in range(len(Mat)):
        for c in range(len(Mat)):
            val = RegleLoc(l,c , Mat )
            NouvMat[l][c] = val
            """if val ==1:
                pygame.draw.line(fenetre, (0,0,255), (coga[0]+l*TailleCotePixel,coga[1]+c*TailleCotePixel),(coga[0]+(l+1)*TailleCotePixel,coga[1]+(c+1)*TailleCotePixel ))
                pygame.display.flip()
                continueee =1
                while continueee:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN and event.key == K_ESCAPE :            #on avance d uncontinuertampon
                            continueee =0"""

    return NouvMat

def dessineMat(Mat):
    for l in range(Cote):
        for c in range(Cote):

            if Mat[l][c]==1:#
                pygame.draw.rect(fenetre, green, (coga[0]+ l*TailleCotePixel +1, coga[1]+ c*TailleCotePixel  +1 ,TailleCotePixel-1, TailleCotePixel-1))
                #pygame.draw.rect(fenetre, green, (coor[0], coor[1], TailleCotePixel, TailleCotePixel)) modele
            if Mat[l][c]==0:
                pygame.draw.rect(fenetre, (0,0,0), (coga[0]+ l*TailleCotePixel  + 1, coga[1]+ c*TailleCotePixel   +1,TailleCotePixel-1,TailleCotePixel-1))

    pygame.display.flip()
    return


continuer =1

while continuer:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE :            #fermeture de la fenetre
            continuer =0
        if  event.type == KEYDOWN and event.key == K_t : #on randomise la si
            Mat_AC = randomMat()
            dessineMat(Mat_AC)
            pygame.display.flip()
        if event.type == KEYDOWN and event.key == K_SPACE:              # on initialise la matrice manuellement
            continuerBis =1
            while continuerBis:
                for event1 in pygame.event.get():
                    if event1.type == KEYDOWN and event1.key == K_r: # on initialise rapidement
                        ContinuerBisBis = 1
                        while ContinuerBisBis:
                            for event2 in pygame.event.get():
                                print("bonjour")
                    val = getClick(event1)
                    if val != None:
                        #print("on est passe le if ")
                        coor = PixelHaGa(val)
                        #print("on est passe le HaGa")
                        #print(coor)
                        #print("on affiche la case")
                        Case = CaseMat(coor)
                        #print(Case)
                        #print("on affiche la matrice ")
                        if Case[0]>=0 and Case[0]<Cote and Case[1]>=0 and Case[1]<Cote:
                            Mat_AC[Case[0]][Case[1]] = 1
                            #afficheMat(Mat_AC)r
                            pygame.draw.rect(fenetre, green, (coor[0], coor[1], TailleCotePixel, TailleCotePixel))
                            pygame.display.flip()
                        else:
                            print("Selectionnez une cellule de l automate")
                    if event1.type == KEYDOWN and event1.key == K_ESCAPE:       # on a fini d initialiser la matrice Mar_AC
                        continuerBis =0

        if event.type == KEYDOWN and event.key == K_g:   # GGGGGo l automate
            #print("on est passe le go ")
            i=0
            continuerBis2 =1
            #BufferMat= copy.deepcopy(Mat_AC)
            while continuerBis2:
                for event in pygame.event.get():

                    if event.type == KEYDOWN and event.key == K_ESCAPE: # on sort de la boucle de travail
                        continuerBis2 =0
                        pygame.display.flip()


                #print("continuerBis2 "+str(i))
                i+=1
                Mat_AC = reinitialise(Mat_AC)
                dessineMat(Mat_AC)
                pygame.display.flip()
                #afficheMat(Mat_AC)
            """ralentisseur=1
                while ralentisseur:
                    for event1 in pygame.event.get():
                        if event1.type == KEYDOWN and event1.key == K_ESCAPE:       # on sort de la simulation
                            continuerBis2 =0
                        if event1.type == KEYDOWN and event1.key ==K_r: #on ralentit slowdown
                            ralentisseur =0"""




