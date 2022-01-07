from math import trunc
import pymysql
from pymysql import cursors
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from datetime import datetime

class student:
    #To insert new student records
    def insert():
        try:
            _json = request.json
            _roll_no = _json['roll_no']
            _first_name = _json['first_name']
            _last_name = _json['last_name']
            _class = _json['class']
            _age = _json['age']
            _address = _json['address']
            _phone = _json['phone']
            _whatsapp = _json['whatsapp']
            # insert record in database
            sqlQuery = "INSERT INTO students(roll_no, first_name, last_name, class, age, address, phone, whatsapp) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (_roll_no, _first_name, _last_name, _class, _age, _address, _phone, _whatsapp)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, data)
            conn.commit()
        
            return jsonify(
                message = 'Student details inserted successfully.',
                status = 200
            )
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    #To list down all students
    def list():
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            #Get records from database table
            sqlQuery = "SELECT * FROM students"
            cursor.execute(sqlQuery)
            rows = cursor.fetchall()
            conn.commit()

            return jsonify(
                data = rows,
                status = 200
            )
        except Exception as e :
            print(e)
        finally:
            cursor.close()
            conn.close()

    #To update student details
    def update():
        try:
            _json = request.json
            _student_id = _json['id']
            _roll_no = _json['roll_no']
            _first_name = _json['first_name']
            _last_name = _json['last_name']
            _class = _json['class']
            _age = _json['age']
            _address = _json['address']
            _phone = _json['phone']
            _whatsapp = _json['whatsapp']
            _status = _json['status']
            _modified_at = datetime.now()

            if _student_id and request.method == 'PUT':
                #Update query for student records
                sqlQuery = "UPDATE students SET roll_no=%s, first_name=%s, last_name=%s, class=%s, age=%s, address=%s, phone=%s, whatsapp=%s, status=%s, modified_at=%s WHERE id=%s"
                data = (_roll_no, _first_name, _last_name, _class, _age, _address, _phone, _whatsapp, _status, _modified_at, _student_id)
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sqlQuery, data)
                conn.commit()

                return jsonify(
                    message = 'Student details updated successfully',
                    status = 200
                )
            else:
                return student.not_found()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    #Get the particular student details by passing id
    def get(student_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "SELECT * FROM students WHERE id=%s"
            cursor.execute(sqlQuery, student_id)
            row = cursor.fetchone()

            return jsonify(
                data = row,
                status = 200
            )
        except Exception as e:
           print(e)
        finally:
            cursor.close()
            conn.close()
    
    #Delete student record 
    def delete(student_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            sqlQuery = "DELETE FROM students WHERE id=%s"
            cursor.execute(sqlQuery, (student_id))
            conn.commit()

            return jsonify(
                message = "Student deleted successfully",
                status = 200
            )
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @app.errorhandler(404)
    def not_found(error=None):
        message = {
            'status': 404,
            'message': 'There is no record: ' + request.url,
        }
        res = jsonify(message)
        res.status_code = 404

        return res

    if __name__ == "__main__":
        app.run(debug=True)