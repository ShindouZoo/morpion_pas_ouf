import turtle as tu

###FONCTION QUI DESSINE UNE GRILLE DE MORPION

def grille():
    tu.pensize(3)
    tu.hideturtle()
    for i in range (4) :
        tu.fd(-180)
        tu.lt(90)

    tu.bk(60)
    tu.lt(90)
    tu.fd(-180)
    tu.lt(90)
    tu.fd(60)
    tu.rt(90)
    tu.fd(180)
    tu.lt(90)
    tu.fd(60)
    tu.lt(90)
    tu.fd(60)
    tu.lt(90)
    tu.fd(180)
    tu.rt(90)
    tu.fd(60)
    tu.rt(90)
    tu.fd(180)



