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

    @staticmethod
    def about():
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "CREATE TABLE IF NOT EXISTS about(id int primary key NOT NULL AUTO_INCREMENT, title VARCHAR(100), banner TEXT NOT NULL, heading VARCHAR(255), sub_title VARCHAR(100) NOT NULl, sub_heading TEXT, mission TEXT NOT NULL, vision TEXT NOT NULL, history TEXT NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, modified_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"
        cursor.execute(sqlQuery)
        print('about table created!\n')

    @staticmethod
    def about_blogs():
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "CREATE TABLE IF NOT EXISTS about_blogs(id int primary key NOT NULL AUTO_INCREMENT, image TEXT NOT NULL, heading VARCHAR(255) NOT NULL, blog_short_desc TEXT NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, modified_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"
        cursor.execute(sqlQuery)
        print('about blogs table created!\n')    

helper = DBHelper()
helper.about()
helper.about_blogs()