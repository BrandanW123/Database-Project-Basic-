import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	passwd="Password",
	database="Deliverable")

mycursor = mydb.cursor()

#List Customers who spent more than $100

mycursor.execute("SELECT CName FROM Customer WHERE LoginName IN (SELECT LoginName FROM Transaction WHERE TotalAmount > 100.00)")

print "Query 1\n"
for x in mycursor:
	print x
print('\n')
#List photos that weren't bought
print "Query 2\n"
mycursor.execute("SELECT PhotoID FROM Photo WHERE TransID IS NULL")
for x in mycursor:
	print x
print('\n')
#List customers who bought photos including specific model
print "Query 3\n"
mycursor.execute("SELECT C.CName FROM Customer C WHERE NOT EXISTS (SELECT * FROM Photo P, Models M WHERE P.PhotoID=M.PhotoID AND M.MName = 'Blake' AND NOT EXISTS (SELECT * FROM Transaction T WHERE T.LoginName=C.LoginName AND T.TransID=P.TransID))")
for x in mycursor:
	print x
print('\n')
print "Query 4\n"

#List Photographers who influences US photographers. 
mycursor.execute("SELECT I.RPName FROM Influences I WHERE I.RPName NOT IN (Select I2.RPName FROM Influences I2, Photographer P WHERE P.PName = I2.EPName AND P.PNationality <> 'US' AND I2.RPname = I.RPName) GROUP BY I.RPName")
for x in mycursor:
	print x