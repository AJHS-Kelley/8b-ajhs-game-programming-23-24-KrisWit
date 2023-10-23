# playerInventory = []

# while len(playerInventory) < 10: 
#     item = input("What item do you want to add to the inventory?\n")
#     playerInventory.append(item)

# playerInventory.sort()
# print(playerInventory)

# while len(playerInventory) > 5:
#     item = input("What item do you want to remove to the inventory?\n")
#     playerInventory.remove(item)

# playerInventory.sort()
# print(playerInventory)

# doorKeys =[
#     "red",
#     "green",
#     "yellow",
#     "purple",
#     "blue"  
# ]

# key = input("Which color key do you need to unlock the door\n")

# if key in doorKeys:
#     print("You have the correct key! The door unlocks.\n")
# else:
#     print("You do not have that key. The door remains locked.\n")

weaponList = [
    True, # Sword
    False, # Laser beam
    False, # Gun that shoots mines
    True, # Teleporter
    False, # RPG
    False, # Air 
    True # Knife
]

weaponNum = 0
while weaponNum < len(weaponList): 
    if weaponNum == 0 and weaponList[0] == True: 
        print("You are wielding a golden sword.\n")
    if weaponNum == 1 and weaponList[1] == True:
        print("You have a laser beam\n")
    if weaponNum == 2 and weaponList[2] == True:
        print("You have a gun that shoots mines\n")
    if  weaponNum == 3 and weaponList[3] == True: 
        print("You have a Teleporter.\n")
    if weaponNum == 4 and weaponList[4] == True: 
        print("You have a RPG.\n")
    if weaponNum == 5 and weaponList[5] == True: 
        print("You Air.\n")
    if weaponNum == 6 and weaponList[6] == True: 
        print("You are wielding a shiny knife.\n")
    weaponNum += 1