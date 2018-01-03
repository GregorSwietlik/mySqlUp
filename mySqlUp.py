#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""Ubuntu16.04.3 -> sudo apt install python-pip libmysqlclient-dev python-dev python-mysqldb python3-mysql.connector"""

db01_host = "db01.domain.com"
db01_user = "user-db01"
db01_password = "xxxxx"

db02_host = "db02.domain.com"
db02_user = "user-db02"
db02_password = "xxxxx"

db01_select = ("SELECT a1, b1, c1 FROM db.table WHERE a1 = 'xxxx'")
db02_truncate = ("TRUNCATE db.table")
db02_insert = ("INSERT INTO db.table (a2, b2, c2) VALUES (%s, %s, %s)")

import mysql.connector 

cnx_db01 = mysql.connector.connect(host=db01_host, user=db01_user, password=db01_password)
db01 = cnx_db01.cursor()
cnx_db02 = mysql.connector.connect(host=db02_host, user=db02_user, password=db02_password)
db02 = cnx_db02.cursor()
db02.execute(db02_truncate)
db01.execute(db01_select)
rows = db01.fetchall()
for row in rows:
	db02.execute(db02_insert, row)
	cnx_db02.commit()
cnx_db01.close()
cnx_db02.close()