import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	passwd="Password",
	database="Deliverable")

mycursor = mydb.cursor()

#Compute Total Sale Per Customers
print("Query 11\n")
mycursor.execute("SELECT SUM(T.TotalAmount),C.CName FROM Transaction T,Customer C WHERE T.LoginName = C.LoginName GROUP BY C.CName")
for x in mycursor:
	print x
print('\n')
#Compute total sales per photographer sorted by photographer
print ("Query 12 \n")
mycursor.execute("SELECT SUM(P.Price),P.Pname FROM Transaction T, Photo P WHERE P.TransID=T.TransID GROUP BY P.PName ORDER BY P.PName")
for x in mycursor:
	print x
print('\n')
#Compute total sales by photo type
print("Query 13\n")
mycursor.execute("SELECT SUM(DISTINCT Portraits.PortraitPrice),SUM(DISTINCT Landscapes.LandscapePrice),SUM(DISTINCT Abstracts.AbstractPrice) FROM (SELECT SUM(P.Price) AS LandscapePrice FROM Transaction T, Photo P, Landscape L WHERE P.PhotoID=L.PhotoID AND P.TransID = T.TransID GROUP BY L.PhotoID) Landscapes, (SELECT SUM(P.Price) AS PortraitPrice FROM Transaction T, Photo P, Models M WHERE T.TransID=P.TransID AND M.PhotoID=P.PhotoID GROUP BY M.PhotoID) Portraits, (SELECT SUM(P.Price) AS AbstractPrice FROM Transaction T, Photo P, Abstract A WHERE T.TransID = P.TransID AND P.PhotoID = A.PhotoID GROUP BY A.PhotoID) Abstracts")
for x in mycursor:
	print x
print('\n')
#Compute top n dates  (in a total sales per date list) 
print("Query 14\n")
mycursor.execute("SELECT SUM(T.TotalAmount),T.TDate FROM Transaction T GROUP BY T.TDate")
for x in mycursor:
	print x