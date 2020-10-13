import os
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platform
      _ = os.system('cls')

#global variables
fname=[]
j=0
c=0

def search():
    print("Enter file name to be searched:")
    fsearch = input()
    temp=[]
    f=1
    temp.append(fsearch)
    for i in fname:
        if(temp == i):
            print("Searched file is present in directory.")
            f=0
    if(f):
        print("Searched file is not present in directory.")
    print("-----------------------------------------------------------------------\n\n")    

def del_file(j):
    print("Enter file name to be deleted:")
    fdel = input()
    temp=[]
    f=1
    temp.append(fdel)
    for i in fname:
        if(temp == i):
            fname.remove(i)
            fname.append([])
            print("File has been deleted from the directory.")
            f=0
    if(f):
        print("\nThe given file is not present in directory.")
    print("-----------------------------------------------------------------------\n\n")    

def display(j):
    if (j==-1):
        print("\nNo file present in the directory.")
    for i in range(0,j,1):
        print(fname[i])
    print("-----------------------------------------------------------------------\n\n")
    
def main():
    j=0
    c=0
    ptemp=[]
    ch=0
    choice=0
    cman=0
    man=0
    name=[]
    screen_clear()
    while(1):
        print("1. Create Directory\t2. Create File\t3. Delete File")
        print("\n4. Search File\t\t5. Display\t6. Exit\n\nEnter your choice -- ")  
        choice = int(input())
        if(choice==1):
            print("\n\nEnter the directory name:")
            dname=input()
            man=1
            print("\n")
        elif(choice==2):
            if(man):
                if(cman != 1):
                    print("Enter the number of files:")
                    nf=int(input())
                    for i in range(nf):
                        fname.append([])
                    cman=1
                k=0
                while(ch==1 or k==0):
                    k=1
                    l=0
                    temp=[]
                    print(fname)
                    print("Enter file name to be created:")
                    name=input()
                    temp.append(name)
                    for i in fname:
                        if(temp == i):
                            print("There is already ",name)
                            break
                        else:
                            l=l+1
                    if(l==nf and j<nf):
                        ptemp=fname[j]
                        if(ptemp!=[] and c>=nf):
                            print("Cannot enter file. Please try again.")
                        else:
                            fname[j].append(name[:])
                            print(fname[j])
                            j=j+1
                            c=c+1
                    if(c<nf):
                        print("Do you want to enter another file(Yes - 1 or No - 0):")
                        ch=int(input())
                    else:
                        print("\nMaximum no. of files have been input.\n")
                        print("Directory name is: ",dname)
                        print("Files names are:")
                        for i in range(j):
                            print(fname[i])
                        break
            else:
                print("Please enter the directory name.\n")
        elif(choice==3):
            if(not man):
                print("Please enter the directory name.\n")
            else:
                del_file(j)
                j=j-1
                c=c-1
        elif(choice==4):
            if(not man):
                print("Please enter the directory name.\n")
            else:
                search()
        elif(choice==5):
            if(not man):
                print("Please enter the directory name.\n")
            else:
                print("Directory name is: ",dname)
                display(j)
        else:
            break

if __name__ == '__main__':
    main()