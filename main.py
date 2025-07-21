from pathlib import Path
import os   #operating system & for delete files



#if the user want to create a file then first the interface will show user the pre-existing files and folders
def readfileandfolder():
    path = Path('')   #empty space will  thegive path of files and folders of the current folder or directory
    items = list(path.rglob('*'))  #recursive glob function will read all the files amd folders and show all items present in that path 
    for i,items in enumerate(items):   #to show index and values separately from a list
        print (f"{i+1} : {items}")




def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name:- ")
        p = Path(name)

        if not p.exists(): #if p not exists (bool type) -> NOT(p.exists)
            with open(p,"w") as fs:  #with is a function 
                data = input("What do you want to write in this file :- ")
                fs.write(data)

            print(f"FILE CREATED SUCCESSFULLY\n")
        else:
            print(f"FILE ALREADY EXISTS:(")
    except Exception as err:
        print(f"An error occured as {err}")



def readfile():
    try: 
        readfileandfolder()
        name = input("Which file you want to read :-")
        p = Path(name)

        if p.exists() and p.is_file():  #p should not be the directory
            with open(p,"r") as fs:
                data = fs.read()
                print(data)

            print(f"READED SUCCESSFULLY")
        else:
            print(f"FILE DOES NOT EXISTS.")
    except Exception as err:
        print(f"An error occured as {err}")
    


def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update :-")
        p = Path(name)

        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending same content in your file")

            res = int(input("Tell your response :- "))
            if (res == 1):
                name2 = input("tell your new file name :- ")
                #p.rename(name2) this can also be done 
                p2 = Path(name2)
                p.rename(p2)

            if(res == 2): 
                with open(p,"w") as fs:
                    data =  input("Tell what you want to write ? This will overwrite your data. : ")
                    fs.write(data) 

            if(res == 3): 
                with open(p,"a") as fs:
                    data =  input("Tell what you want to write ? This will append your data. : ")
                    fs.write(" "+data) 

    except Exception as err:
        print(f"An error occured as {err}")

            

def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete ?")
        p = Path(name)
        
        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfully.")
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"An error occured as {err}")




print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion of a file")

check = int(input("Please tell your response : "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()



    