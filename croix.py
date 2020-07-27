import turtle as tu


def croix():
    tu.pencolor("red")
    tu.pendown()
    tu.hideturtle()
    tu.pensize(3)

    tu.setheading(45)
    tu.fd(60)
    tu.penup()

    tu.rt(135)
    tu.fd(43)
    tu.pendown()
    tu.rt(135)
    tu.fd(60)



def case_croix():
        cc=float(input("case : "))
        tu.penup()
        if cc==1 :
            tu.goto(-170,-55)
            croix()
        elif cc==2 :
            tu.goto(-110,-55)
            croix()
        elif cc==3 :
            tu.goto(-50,-55)
            croix()
        elif cc ==4 :
            tu.goto(-170,-115)
            croix()
        elif cc==5 :
            tu.goto(-110,-115)
            croix()
        elif cc==6 :
            tu.goto(-50,-115)
            croix()
        elif cc==7 :
            tu.goto(-170,-175)
            croix()
        elif cc==8 :
            tu.goto(-110,-175)
            croix()
        elif cc==9 :
            tu.goto(-50,-175)
            croix()
        
            

