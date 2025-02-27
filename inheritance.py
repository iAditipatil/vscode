class student:
    def __init__(self,rollno,name):
        self.roll=rollno
        self.nm=name

    def print1(self):
        print("rollno=",self.roll,"name=",self.nm)

class stdinfo(student):
    def __init__(self,rollno,name,age):
        self.agee=age
        super().__init__(rollno,name)
    def print2(self):
        print("age=",self.agee)
s1=stdinfo(1,"amit",34)
s1.print1()
s1.print2()

        