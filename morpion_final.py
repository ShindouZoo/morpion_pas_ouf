########### IMPORTATION DES MODULES ##########
from grille_morpion import *
from croix import *
from rond import *
import turtle as tu
import sys

######### FONCTIONS ##########
print ("LE JEU VA COMMENCER")


def morpion() :
    grille()
    case_croix()
    case_rond()
    case_croix()
    case_rond()
    case_croix()
    case_rond()
    case_croix()
    case_rond()
    case_croix()
    

def recommencer():
    r=input ("recommencer la partie ? : ")
    
    if r=="oui" :
             tu.reset()
             morpion()

    if r=="non" :
            print ("La partie est terminée")
            tu.reset()
        
    else :
        print ("IL FAUT REPONDRE 'oui' OU 'non'")
        return recommencer()
        
    


################## PROGRAMME PRINCIPAL #############
morpion()
recommencer()




    

