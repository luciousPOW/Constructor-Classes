class Character:
    def __init__(self,name,hp,mp,atk,lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl
        
name = input("Enter name: ")
hp = int(input("Enter HP: "))
mp = int(input("Enter MP: "))
atk = int(input("Enter ATK: "))
lvl = int(input("Enter level: "))

userInput = Character(name,hp,mp,atk,lvl)

print("Character Attributes: ")
print("Name:", name)
print("HP:", hp)
print("MP:", mp)
print("Attack:",atk)
print("Level:",lvl)

