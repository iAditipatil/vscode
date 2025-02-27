f=open("CDesktop\python\write.txt","W+") 
#Write contents in file 
f.write("JAVA \n") 
f.write("PYTHON \n") 
f.write("Big Data \n") 
f.write("R \n") 
#reading file 
f.seek(0) 
print(f.read()) 