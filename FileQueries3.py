# -*- coding: utf-8 -*-

import mysql.connector
import sys
reload(sys)
sys.setdefaultencoding('utf8')


mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	passwd="Password",
	database="Deliverable")

mycursor = mydb.cursor()

#Rank the photos by the Sum of Prices of the photos they took
print("Query 8\n")
mycursor.execute("SELECT SUM(H.Price),P.PName FROM Photographer P, Photo H WHERE P.PName=H.PName GROUP BY P.PName ORDER BY SUM(H.Price) DESC")
for x in mycursor:
	print x
print('\n')
#Delete specific photo
print("Query 9\n")
mycursor.execute("DELETE FROM Photo P WHERE P.PhotoID = 32323365")
for x in mycursor:
	print x
print('\n')
print("Query 10\n")
#Update photographer of specific photo to different photographer
mycursor.execute("UPDATE Photo SET `PName` = 'Joy', `PBDate`= '1970-05-11' WHERE PhotoID=56878821")
mycursor.execute("SELECT PName FROM Photo WHERE PhotoID=56878821")
for x in mycursor:
	print x
