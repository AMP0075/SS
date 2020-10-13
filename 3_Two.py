import os
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platform
      _ = os.system('cls')

def main():
    d={}
    fcnt={}
    dcnt=0
    while(True):
        print("\n1. Create Directory\n2. Delete Directory\n3. Create File\n4. Delete File\n5. Search File\n6. Display Files\n7. Exit");
        ch=int(input("Enter your choice -- "))
        if(ch==1):
            dname=input("Enter name of the directory : ")
            if dname in d:
                print("There is already another directory with the same name.")
            else:
                d[dname]=[]
                fcnt[dname]=0
                dcnt+=1
                print("Directory created successfully.")
            continue
        elif(ch==2):
            if(dcnt!=0):
                dname=input("Enter name of the directory : ")
                if dname in d:
                    if(fcnt[dname]==0):
                        d.pop(dname)
                        fcnt.pop(dname)
                        dcnt-=1
                        print("Directory has been deleted.")
                    else:
                        print("Directory is not empty, cannot delete a non-empty directory.")
                else:
                    print("Sorry, Directory not found.")
            else:
                print("No User Directories Found, Root Directory is empty.");
            continue
        elif(ch==3):
            if(dcnt!=0):
                dname=input("Enter name of the directory: ")
                if dname in d:
                    fname=input("Enter name of the file: ")
                    if fname in d[dname]:
                        print("There is already another file with the same name in this directory!!")
                    else:
                        d[dname].append(fname)
                        fcnt[dname]+=1
                        print("File created successfully in the directory : ",dname)
                else:
                    print("Sorry, Directory not found.")
            else:
                print("No User Directories Found, Root Directory is empty.");
            continue    
        elif(ch==4):
            if(dcnt!=0):
                dname=input("Enter name of the directory : ")
                if dname in d:
                    fname=input("Enter name of the file : ")
                    if fname in d[dname]:
                        d[dname].remove(fname)
                        fcnt[dname]-=1
                        print("File was found and deleted successfully from the directory : ",dname)
                    else:   
                        print("Sorry, File not found.")
                else:
                    print("Sorry, Directory not found.")
            else:
                print("No User Directories Found, Root Directory is empty.");
            continue
        elif(ch==5):
            if(dcnt!=0):
                dname=input("Enter name of the directory : ")
                if dname in d:
                    fname=input("Enter name of the file : ")
                    if fname in d[dname]:
                        print("File is present in the directory : ",dname)
                    else:
                        print("Sorry, File not found.")
                else:
                    print("Sorry, Directory not found.")
            else:
                print("No User Directories Found, Root Directory is empty.");
            continue
        elif(ch==6):
            if(dcnt!=0):
                print("\nDirectory --> Files")
                print("----------------------------------------------------------\n")
                for dname in d:
                    print(dname,"--> ",end="")
                    for fname in d[dname]:
                        print(fname,end=" ")
                        print("\n")
                print("----------------------------------------------------------\n")
            else:
                print("No User Directories Found, Root Directory is empty.");
            continue
        else:
            break

if __name__ == '__main__':
    main()