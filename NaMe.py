import random
def FiLe():
    name= input("What is the name of the folder-name you are going to use?\t")
    ID=input("would you like to use an Identifier? (y/n)?")
    if ID =="y":
        ID=str("[%d]"%random.randint(1,15))
        File_Name=name+ID
        return File_Name
    if ID =="n":
        File_Name=name
        return File_Name
    else:
        File_Name=name
        return File_Name
