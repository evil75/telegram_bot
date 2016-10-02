#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
from creditails import *
def select (chatId):
	conn = psycopg2.connect(database=dbName, user=dbUser, password=dbPass, host=dbHost, port=dbPort)
	cur = conn.cursor()
	cur.execute("SELECT * FROM %s where chatid = %s;" % (dbTable, chatId)
	all=cur.fetchall()
	conn.commit()
	cur.close()
	conn.close() 
	string=''
	for resalt in all:
		string=string + str(resalt[0]) + ' Название: ' + str(resalt[1]) + ' ' + 'Описание: ' + str(resalt[2]) + ' ' + 'Предложено: ' + str(resalt[3]) + '\n'
	if string == '':
		string='Не чего показать=(('
	else:
		string += 'теперь ты видел все=))'
	return string
def insert (name, description, author, chatId):
	conn = psycopg2.connect(database=dbName, user=dbUser, password=dbPass, host=dbHost, port=dbPort)
	cur = conn.cursor()
	cur.execute("INSERT INTO events (name, description, author, chatid) VALUES (%s, %s, %s, %s)", (name, description, author, chatId))
	conn.commit()
    	cur.close()
    	conn.close()

def delete (id):
	conn = psycopg2.connect(database=dbName, user=dbUser, password=dbPass, host=dbHost, port=dbPort)
	cur = conn.cursor()
	cur.execute("DELETE FROM events WHERE id=%s;", [id])
	conn.commit()
	cur.close()
	conn.close()
