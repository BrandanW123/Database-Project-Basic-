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

#List Photographers who only took portrait photos
print("Query 5\n")
mycursor.execute("SELECT P.PName FROM Photographer P, Photo H WHERE P.PName = H.PName AND H.PName NOT IN ((SELECT h2.PName FROM Photo h2, Landscape L WHERE L.PhotoID=h2.PhotoID) UNION (SELECT h3.PName FROM Photo h3, Abstract A WHERE A.PhotoID=h3.PhotoID))")
for x in mycursor:
	print x
print('\n')

#List transactions which contain more than 3 photos
print("Query 6\n")
mycursor.execute ("SELECT T.TransID FROM Transaction T, Photo P WHERE T.TransID = P.TransID GROUP BY T.TransID HAVING COUNT(P.PhotoID) > 3")
for x in mycursor:
	print x
print('\n')
#List models who modeled in all photos taken by a specific Photographer
print("Query 7\n")
mycursor.execute("SELECT M.MName FROM Models M, Photo PH, Photographer P WHERE (M.PhotoID = PH.PhotoID) AND PH.PName=P.PName AND PH.PhotoID IN (SELECT PhotoID FROM Photo WHERE PName = 'Alice')")
for x in mycursor:
	print x