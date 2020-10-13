import os
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platform
      _ = os.system('cls')
def main():
    f=[]
    index=[] 
    c=1
    n=0
    count=0
    screen_clear()
    for i in range(50):
        f.append(0)
    while c:
        x=1
        y=1
        while x:
            print("Enter the index block: ")
            ind = int(input())
            if(f[ind]!=1):
                print("Enter no of blocks needed and no of files for the index ",ind," on the disk : \n")
                n = int(input())
                break
            else:
                print(ind," Index is already allocated \n")
                x=1
        while y:
            count=0
            index=[]
            for i in range(0,n,1):
                index.append(int(input()))
                if(f[index[i]]==0):
                    count=count+1
            if(count==n):
                for j in range(n):
                    f[index[j]]=1
                print("Allocated\n")
                print("File Indexed\n")
                for k in range(n):
                    print(ind," -------->",index[k]," : ",f[index[k]],"\n")
                break
            else:
                print("File in the index is already allocated \n")
                print("Enter another file indexed")
                y=1
        print("Do you want to enter more file(Yes - 1/No - 0)")
        c = int(input())
        if(c!=1):
            break
            
if __name__ == '__main__':
    main()