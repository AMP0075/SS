import os
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platform
      _ = os.system('cls')

screen_clear()
N = int(input("Enter the size of Buffer : "))

def wait(s):
	try:
		while(s<0):
			pass
		s-=1
		return(s)
	except:
		print("Integer input only.")

def signal(s):
	try:
		s+=1
		return(s)
	except:
		print("Integer input only.")

def producer(n):
	global buff, mlock
	mlock = wait(mlock)
	buff += [n]
	mlock = signal(mlock)
	print("Process added to buffer")

def consumer(n):
	global buff,mlock
	mlock = wait(mlock)
	value = buff.pop(buff.index(n))
	mlock = signal(mlock)
	print("Process removed from buffer")

def main():
	choice = int(input("\n1.Produce\n2.Consume\n3.Exit:\n"))
	if(choice==1):
		if(mlock==1 and len(buff)!=N):
			producer(1)
		else:
			print("Buffer is full\n")
	elif(choice==2):
		if(mlock==1 and len(buff)!=0):
			consumer(1)
		else:
			print("Buffer is empty\n")
	else:
		exit()

if __name__ == '__main__':
    mlock = 1
    buff  = []
    while(1):
        main()