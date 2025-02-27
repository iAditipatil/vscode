class addition:
    def __init__(self,*args):

        if(len(args)==2):

            add=args[0]+args[1]
            print("additi of",args[0],"+",args[1],"=",add)

        elif(len(args)==3):
            add=args[0]+args[1]+args[2]
            print("additi of",args[0],"+",args[1],"+",args[2],"=",add)
a1=addition(2,3)
a2=addition(2,3,4)