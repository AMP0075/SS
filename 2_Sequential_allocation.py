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
    c=1
    count = 0
    screen_clear()
    for i in range(50):
        f.append(0)
    print("Files Allocated are : \n")
    while c:
        count=0
        print("Enter starting block and length of files: ")
        st=int(input())
        len=int(input())
        for k in range(st,(st+len)):
            if(f[k]==0):
                count=count+1
        if(len==count):
            for j in range(st,(st+len)):
                if(f[j]==0):
                    f[j]=1
                    print(j,"\t",f[j],"\n")
            if(j!=(st+len)):
                print("The file is allocated to disk\n")
        else:
            print("The file cannot be allocated as the blocks are already allocated.\n")
        print("Do you want to enter more file(Yes - 1  /  No - 0)")
        c = int(input())
        if(c!=1):
            break
if __name__ == '__main__':
    main()