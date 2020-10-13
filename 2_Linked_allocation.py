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
    screen_clear()
    for i in range(50):
        f.append(0)
    print("Enter how many blocks already allocated: ");
    p=int(input())
    print("Enter blocks already allocated: ");
    for i in range(p):
        a=int(input())
        f[a]=1
    while c:
        print("Enter index starting block and length: ")
        st=int(input())
        len=int(input())
        k=len
        if(f[st]==0):
            for j in range(st,(st+k)):
                if(f[j]==0):
                    f[j]=1
                    print(j," --------> ",f[j],"\n")
                else:
                    print(j," Block is already allocated \n")
                    k=k+1
        else:
            print(st," starting block is already allocated \n")
        print("Do you want to enter more file(Yes - 1/No - 0)")
        c=int(input())
        if(c!=1):
            break
            
if __name__ == '__main__':
    main()