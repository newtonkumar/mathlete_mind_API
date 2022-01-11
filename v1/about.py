import pymysql
from pymysql.cursors import Cursor
from app import app
from settings.config import mysql
from flask import jsonify, request
from datetime import date, datetime

class about:
    def details():
        try:
            #todo get details from about tables
            return jsonify(
                data = [],
                message = 'About Data',
                status = 200
            )
        except Exception as e:
            print(e)
        finally:
            pass
    
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