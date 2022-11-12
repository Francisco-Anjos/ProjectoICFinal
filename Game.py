import random 

#Player and enemy class stats in order(health,Mana,Armor,Weapon,Initiative)
WarriorClass = ["Warrior",32,5,2,5,2]
PriestClass = ["Priest",20,25,0,2,6]
OrcClass1 = ["Orc1",15,0,2,2,2]
OrcClass2 = ["Orc2",15,0,2,2,2]
OrcClass3 = ["Orc3",15,0,2,2,2]
OrcClass4 = ["Orc4",15,0,2,2,2]
ClassList = [PriestClass,WarriorClass,OrcClass1,OrcClass2,OrcClass3,OrcClass4]


#Action phases per player class and enemy class 
#Warriorclass turn 
def WarriorTurn(HP1,HP2,HP3,HP4,WP,MP,AP1,AP2,AP3,AP4):
    print("Choose your action")
    print("1:Magic")
    print("2:Attack")
    Action = input()
    if Action == "1":
        print("Choose your Spell")
        print("1:Rushdown(Rush at a target and strike them)")
        Spell = input()
        if Spell == "1":
            Target = input("Choose target:")
            if Target == "1":
                print("You casted Rushdown on the first Orc")
                MP = MP - 5
                HP1 = HP1 - ((WP + random.ranint(1,5)))
            elif Target == "2":
                print("You casted Rushdown on the second Orc")
                MP = MP - 5
                HP2 = HP2 - ((WP + random.ranint(1,5)))
            elif Target == "3":
                print("You casted Rushdown on the third Orc")
                MP = MP - 5
                HP3 = HP3 - ((WP + random.ranint(1,5)))
            elif Target == "4":
                print("You casted Rushdown on the forth Orc")
                MP = MP - 5
                HP4 = HP4 - ((WP + random.ranint(1,5)))
    elif Action =="2":
         Target = input("Choose target:")
         if Target == "1":
            print("You struck the first Orc")
            HP1 = HP1 - (WP - AP1)
         elif Target == "2":
            print("You struck the second Orc")
            HP2 = HP2 - (WP - AP2)
         elif Target == "3":
            print("You struck the third Orc")
            HP3 = HP3 - (WP - AP3)
         elif Target == "4":
            print("You struck the forth Orc")
            HP4 = HP4 - (WP - AP4)
            return(HP1,HP2,HP3,HP4,MP)

#Priestclass Turn 
def PriestTurn(HP1,HP2,HP3,HP4,HP5,HP6,WP,MP,AP1,AP2,AP3,AP4):
    print("Choose your action.")
    print("1:Magic")
    print("2:Attack")
    Action = input()
    if Action == "1":
        print("Choose your Spell")
        print("1:Mend(Heal target player)")
        print("2:Exorcism(Exorcise target enemy dealing damage)")
        Spell = input()
        if Spell == "1":
            Target = input("Choose target:")
            if Target == "1":
                print("You mended your wounds.")
                MP = MP - 3
                HP5 = HP5 + (random.randint(1,7)+ WP)
            elif Target == "2":
                print("You mended your wounds.")
                MP = MP - 3
                HP6 = HP6 + (random.randint(1,7) + WP)
        elif Spell == "2":
            Target = input("Choose target:")
            if Target == "1":
                print("You casted Exorcism on the first Orc.")
                HP1 = HP1 - (random.randint(1,5) * 2)
                MP = MP - 5
            elif Target == "2":
                print("You casted Exorcism on the second Orc.")
                HP2 = HP2 - (random.randint(1,5) * 2)
                MP = MP - 5
            elif Target == "3":
                print("You casted Exorcism on the third Orc.")
                HP3 = HP3 - (random.randint(1,5) * 2)
                MP = MP - 5
            elif Target == "4":
                print("You casted Exorcism on the forth Orc.")
                HP4 = HP4 - (random.randint(1,5) * 2)
                MP = MP - 5
    elif Action =="2":
         Target = input("Choose target:")
         if Target == "1":
            print("You struck the first Orc.")
            HP1 = HP1 - (WP - AP1)
         elif Target == "2":
            print("You struck the second Orc.")
            HP2 = HP2 - (WP - AP2)
         elif Target == "3":
            print("You struck the third Orc.")
            HP3 = HP3 - (WP - AP3)
         elif Target == "4":
            print("You struck the forth Orc.")
            HP4 = HP4 - (WP - AP4)
            return(HP1,HP2,HP3,HP4,HP5,HP6,MP)

#The enemy Orc turns
#Orc1
def Orc1Turn(HP1,HP2,WP,AP1,AP2):
            print("The first Orc strikes!")
            print(random.random())
            if random.ramdom == 0:
             HP1 = HP1 - (WP -AP1)
            elif random.ramdom == 1:
             HP2 = HP2 - (WP -AP2)
            return(HP1,HP2)  

#Orc2
def Orc2Turn(HP1,HP2,WP,AP1,AP2):
            print("The Second Orc strikes!")
            print(random.random())
            if random.ramdom == 0:
             HP1 = HP1 - (WP -AP1)
            elif random.ramdom == 1:
             HP2 = HP2 - (WP -AP2)
            return(HP1,HP2) 

#Orc3    
def Orc3Turn(HP1,HP2,WP,AP1,AP2):
            print("The third Orc strikes!")
            print(random.random())
            if random.ramdom == 0:
             HP1 = HP1 - (WP -AP1)
            elif random.ramdom == 1:
             HP2 = HP2 - (WP -AP2)
            return(HP1,HP2)

#Orc4
def Orc4Turn(HP1,HP2,WP,AP1,AP2):
            print("The forth Orc strikes!")
            print(random.random())
            if random.ramdom == 0:
             HP1 = HP1 - (WP -AP1)
            elif random.ramdom == 1:
             HP2 = HP2 - (WP -AP2)
            return(HP1,HP2)          