import random 
#Action phases per player class and enemy class 
#Warriorclass turn 
def WarriorTurn(HP,WP,MP,AP,Rd):
    print("Choose your action")
    print("1:Magic")
    print("2:Attack")
    Action = input()
    if Action == 1:
        print("Choose your Spell")
        print("1:Rushdown")
        Spell = input()
        if Spell == 1:
            Target = input("Choose target:")
            if Target == 1:
                print("You casted Rushdown on the first Orc")
                MP = MP - 5
                HP = HP - ((WP + Rd)-AP)
            elif Target == 2:
                print("You casted Rushdown on the second Orc")
                MP = MP - 5
                HP = HP - ((WP + Rd)-AP)
            elif Target == 3:
                print("You casted Rushdown on the third Orc")
                MP = MP - 5
                HP = HP - ((WP + Rd)-AP)
    elif Action ==2:
         Target = input("Choose target:")
         if Target == 1:
            print("You struck the first Orc")
            HP = HP - (WP - AP)
            return(HP,MP)
         elif Target == 2:
            print("You struck the second Orc")
            HP = HP - (WP - AP)
            return(HP,MP)
         elif Target == 3:
            print("You struck the third Orc")
            HP = HP - (WP - AP)
            return(HP,MP)


#Priestclass Turn 
def PriestTurn(HP,WP,MP,AP,Ex,He):
    print("Choose your action")
    print("1:Magic")
    print("2:Attack")
    Action = input()
    if Action == 1:
        print("Choose your Spell")
        print("1:Mend")
        print("2:Exorcism")
        Spell = input()
        if Spell == 1:
            Target = input("Choose target:")
            if Target == 1:
                print("You healed yourself")
                MP = MP - 3
                HP = HP + (He + WP )
            elif Target == 2:
                print("You healed yourself")
                MP = MP - 3
                HP = HP + (He + WP )
        elif Spell == 2:
            Target = input("Choose target:")
            if Target == 1:
                print("You casted Exorcism")
                HP = HP - (Ex - AP)
                MP = MP - 5
            elif Target == 2:
                print("You casted Exorcism")
                HP = HP - (Ex - AP)
                MP = MP - 5
            elif Target == 2:
                print("You casted Exorcism")
                HP = HP - (Ex - AP)
                MP = MP - 5
    elif Action ==2:
         Target = input("Choose target:")
         if Target == 1:
            print("You struck the first Orc")
            HP = HP - (WP - AP)
            return(HP,MP)
         elif Target == 2:
            print("You struck the second Orc")
            HP = HP - (WP - AP)
            return(HP,MP)
         elif Target == 3:
            print("You struck the third Orc")
            HP = HP - (WP - AP)
            return(HP,MP)

#The enemy Orc turns
def Orc1Turn(HP,WP,AP):
            print("The first Orc strikes!")
            print(random.random())
            HP = HP - (WP -AP)
            return(HP)  


def Orc2Turn(HP,WP,AP):
            print("The Second Orc strikes!")
            print(random.random())
            HP = HP - (WP -AP)
            return(HP) 

    
def Orc3Turn(HP,WP,AP):
            print("The third Orc strikes!")
            print(random.random())
            HP = HP - (WP -AP)
            return(HP)        