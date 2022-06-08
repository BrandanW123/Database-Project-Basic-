# -*- coding: utf-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Password",
	)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Deliverable")

