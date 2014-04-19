#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as sql
import MySQLdb.cursors as cursors
import traceback
import random, sys
from ConfigParser import ConfigParser

# load the database configuration
SQL = "mysql"
config = ConfigParser()
config.read("marathon.cnf")

def GetConnection():
	"""
	Retrieves a connection to the MySQL database, example:
	
		from marathon.database import GetConnection
		connection = GetConnection()
		cursor = connection.cursor()
		query = "select version();"
		try:
			if cursor.execute(query):
				print cursor.fetchall()
		except Exception as e:
			print "Error:", e
		finally:
			cursor.close()
			connection.close()
	"""
    conn = None
    try:
        conn = sql.connect(
        	config.get(SQL, "host"), 
        	config.get(SQL, "user"), 
        	config.get(SQL, "pass"), 
        	config.get(SQL, "database"), 
        	cursorclass=cursors.DictCursor)
        return conn
    except Exception as e:
        if conn:
            conn.close()      
        print "Error: %s" % e
        return None