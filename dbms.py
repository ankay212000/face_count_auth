# importing module 
from pymongo import MongoClient 

def send(name,date,rollno,workstation=0,login=0,logout=0,AU=0,image=0):
	
	# Connect with the portnumber and host 
	client=MongoClient("localhost", 27017)

	# Access database 
	mydatabase = client["data1"] 

	# Access collection of the database 
	mycollection=mydatabase["mytable"] 

	# dictionary to be added in the database 
	record={ 
	"Name":name,"Date":date,"Rollno":rollno,"Workstation":workstation,"Login":login,"Logout":logout,"AU":AU,"Image":image
	} 

	# inserting the data in the database 
	rec = mydatabase.myTable.insert(record) 
