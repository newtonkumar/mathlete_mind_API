import pymysql
from app import app
from settings.config import mysql

class DBHelper:
    def __init__(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = 'CREATE TABLE IF NOT EXISTS students(id int primary key NOT NULL AUTO_INCREMENT,roll_no VARCHAR(100) NOT NULL, first_name VARCHAR(100) NOT NULL, last_name VARCHAR(100), class VARCHAR(50) NOT NULL, age INT, address TEXT NOT NULL, phone VARCHAR(20) NOT NULL, whatsapp VARCHAR(20), status BOOLEAN NOT NULL DEFAULT 0)'
        cursor.execute(sqlQuery)
        print('Student Table Created!\n')


helper = DBHelper()