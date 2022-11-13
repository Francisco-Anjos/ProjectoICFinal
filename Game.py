import random 

#Player and enemy class stats in order(Name,health,Mana,Armor,Weapon,Initiative,Initiativecounter)
WarriorClass = ["Warrior",32,5,2,5,2,0]
PriestClass = ["Priest",20,25,0,2,6,0]
OrcClass1 = ["Orc1",15,0,2,2,2,0]
OrcClass2 = ["Orc2",15,0,2,2,2,0]
OrcClass3 = ["Orc3",15,0,2,2,2,0]
OrcClass4 = ["Orc4",15,0,2,2,2,0]
ClassList = [PriestClass,WarriorClass,OrcClass1,OrcClass2,OrcClass3,OrcClass4]

#Initiative rolls
def RollInit(Class):
    Init = random.randint(1,21) + Class[5]
    Class[6] = Init

def InitFase (ListOfCharacter):
    for Class in ListOfCharacter:
        RollInit(Class)


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
                if HP1 <= 0:
                    HP1 = 0
                    print( "you have killed the first Orc")
            elif Target == "2":
                print("You casted Rushdown on the second Orc")
                MP = MP - 5
                HP2 = HP2 - ((WP + random.ranint(1,5)))
                if HP2 <= 0:
                    HP2 = 0
                    print( "you have killed the second Orc")
            elif Target == "3":
                print("You casted Rushdown on the third Orc")
                MP = MP - 5
                HP3 = HP3 - ((WP + random.ranint(1,5)))
                if HP3 <= 0:
                    HP3 = 0
                    print( "you have killed the third Orc")
            elif Target == "4":
                print("You casted Rushdown on the forth Orc")
                MP = MP - 5
                HP4 = HP4 - ((WP + random.ranint(1,5)))
                if HP4 <= 0:
                    HP4 = 0
                    print( "you have killed the forth Orc")
    elif Action =="2":
         Target = input("Choose target:")
         if Target == "1":
            print("You struck the first Orc")
            HP1 = HP1 - (WP - AP1)
            if HP1 <= 0:
                HP1 = 0
                print( "you have killed the first Orc")
         elif Target == "2":
            print("You struck the second Orc")
            HP2 = HP2 - (WP - AP2)
            if HP2 <= 0:
                HP2 = 0
                print( "you have killed the second Orc")
         elif Target == "3":
            print("You struck the third Orc")
            HP3 = HP3 - (WP - AP3)
            if HP3 <= 0:
                HP3 = 0
                print( "you have killed the third Orc")            
         elif Target == "4":
            print("You struck the forth Orc")
            HP4 = HP4 - (WP - AP4)
            if HP4 <= 0:
                HP4 = 0
                print( "you have killed the forth Orc")
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
                if HP1 <= 0:
                    HP1 = 0
                    print( "you have killed the first Orc")
            elif Target == "2":
                print("You casted Exorcism on the second Orc.")
                HP2 = HP2 - (random.randint(1,5) * 2)
                MP = MP - 5
                if HP2 <= 0:
                    HP2 = 0
                    print( "you have killed the second Orc")
            elif Target == "3":
                print("You casted Exorcism on the third Orc.")
                HP3 = HP3 - (random.randint(1,5) * 2)
                MP = MP - 5
                if HP3 <= 0:
                    HP3 = 0
                    print( "you have killed the third Orc")
            elif Target == "4":
                print("You casted Exorcism on the forth Orc.")
                HP4 = HP4 - (random.randint(1,5) * 2)
                MP = MP - 5
                if HP4 <= 0:
                    HP4 = 0
                    print( "you have killed the forth Orc")
    elif Action =="2":
         Target = input("Choose target:")
         if Target == "1":
            print("You struck the first Orc.")
            HP1 = HP1 - (WP - AP1)
            if HP1 <= 0:
                HP1 = 0
                print( "you have killed the first Orc")
         elif Target == "2":
            print("You struck the second Orc.")
            HP2 = HP2 - (WP - AP2)
            if HP2 <= 0:
                HP2 = 0
                print( "you have killed the second Orc")            
         elif Target == "3":
            print("You struck the third Orc.")
            HP3 = HP3 - (WP - AP3)
            if HP3 <= 0:
                HP3 = 0
                print( "you have killed the third Orc")
         elif Target == "4":
            print("You struck the forth Orc.")
            HP4 = HP4 - (WP - AP4)
            if HP4 <= 0:
                HP4 = 0
                print( "you have killed the forth Orc")
            return(HP1,HP2,HP3,HP4,HP5,HP6,MP)

#The enemy Orc turns
#Orc1
def Orc1Turn(HP1,HP2,WP,AP1,AP2):
            print("The first Orc strikes!")
            print(random.randint(1,3))
            if random.randint == 1:
             HP1 = HP1 - (WP -AP1)
            elif random.randint == 2:
             HP2 = HP2 - (WP -AP2)
            return(HP1,HP2)  

#Orc2
def Orc2Turn(HP1,HP2,WP,AP1,AP2):
            print("The Second Orc strikes!")
            print(random.randint(1,3))
            if random.randint == 1:
             HP1 = HP1 - (WP -AP1)
            elif random.randint == 2:
             HP2 = HP2 - (WP -AP2)
            return(HP1,HP2)  

#Orc3    
def Orc3Turn(HP1,HP2,WP,AP1,AP2):
            print("The third Orc strikes!")
            print(random.randint(1,3))
            if random.randint == 1:
             HP1 = HP1 - (WP -AP1)
            elif random.randint == 2:
             HP2 = HP2 - (WP -AP2)
            return(HP1,HP2)  

#Orc4
def Orc4Turn(HP1,HP2,WP,AP1,AP2):
            print("The forth Orc strikes!")
            print(random.randint(1,3))
            if random.randint == 1:
             HP1 = HP1 - (WP -AP1)
            elif random.randint == 2:
             HP2 = HP2 - (WP -AP2)
            return(HP1,HP2)  

#main game loop 
while (OrcClass1[1]+OrcClass2[1]+OrcClass3[1]+OrcClass4[1]<= 0 or WarriorClass[1]<=0 and PriestClass[1]<=0):
    #New init value for each class
   InitFase(ClassList)

    #Sortint by the rolls   
   ClassList.sort(key = lambda CL:CL[6]) #lambda sorts CL[6] inside ListCLass, like for function 
   print(ClassList[0][0], ClassList[1][0])
#Action turn 
   for i in ClassList:
        if i[6] == WarriorClass[6]: #HP1,HP2,HP3,HP4,WP,MP,AP1,AP2,AP3,AP4
            Warrior = WarriorTurn(OrcClass1[1], OrcClass2[1], OrcClass3[1], OrcClass4[1], WarriorClass[4], WarriorClass[2], OrcClass1[3],OrcClass2[3],OrcClass3[3],OrcClass4[3])
            if WarriorClass[1] <= 0:
                print("You have died.")
                break
        elif i[6] == PriestClass[6]: #HP1,HP2,HP3,HP4,HP5,HP6,WP,MP,AP1,AP2,AP3,AP4 
            Priest = PriestTurn(OrcClass1[1], OrcClass2[1], OrcClass3[1], OrcClass4[1], WarriorClass[1], PriestClass[1], PriestClass[4], PriestClass[2],OrcClass1[3],OrcClass2[3],OrcClass3[3],OrcClass4[3] )
            if PriestClass[1] <= 0:
                print("You have died.")
                break
        elif i[6] == OrcClass1[6]: #HP1,HP2,WP,AP1,AP2
            orc1 = Orc1Turn(WarriorClass[1], PriestClass[1], OrcClass1[4], WarriorClass[3], PriestClass[3])
            if OrcClass1[1] <= 0:
              pass 
        elif i[6] == OrcClass2[6]: #HP1,HP2,WP,AP1,AP2
            orc2 = Orc2Turn(WarriorClass[1], PriestClass[1], OrcClass2[4], WarriorClass[3], PriestClass[3])
            if OrcClass2[1] <= 0:
              pass 
        elif i[6] == OrcClass3[6]: #HP1,HP2,WP,AP1,AP2
            orc3 = Orc3Turn(WarriorClass[1], PriestClass[1], OrcClass3[4], WarriorClass[3], PriestClass[3])
            if OrcClass3[1] <= 0:
              pass 
        elif i[6] == OrcClass4[6]: #HP1,HP2,WP,AP1,AP2
            orc4 = Orc4Turn(WarriorClass[1], PriestClass[1], OrcClass4[4], WarriorClass[3], PriestClass[3])
            if OrcClass4[1] <= 0:
              pass 
        elif(OrcClass1[1] + OrcClass1[1] + OrcClass1[1] + OrcClass1[1] = 0 ):
            print("You won.")
            break

print("Thank you for Playing!")