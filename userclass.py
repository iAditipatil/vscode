class emp:
   

    def display(self,ssn=0,name="",rollno=0):
        self.ssn=ssn
        self.name=name
        self.rollno=rollno
    print("ssn=",{self.ssn},"name=",name,"rollno",rollno)
e1=emp(11,"amit",2)
e1.display()

