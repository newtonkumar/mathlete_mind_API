# mathlete_mind_API
Mathlete Mind EdTech API : Flask Python based For Micro Web services and mobile app development

@Licenced to Newton Kumar Jan 2022 India

Step 1 : Git clone to project
Step 2 : Install all dependecies by the help of requirements.txt
Step 3 : Run if not having mysql server **sudo apt-get install mysql-server** also **sudo mysql_secure_installation utility**
Step 4 : Run command **sudo ufw enable** for activating Firewall and enabled on system startup
Step 5 : Run command **sudo ufw allow mysql** for mysql rule activation
Step 6 : **sudo systemctl start mysql**
Step 7 : **sudo systemctl enable mysql**
Step 8 : Run **sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf** to add 
Step 9 : Restart the mysql services **sudo systemctl restart mysql** and check the status for verification **sudo systemctl status mysql**
Step 10 : Run command **sudo /usr/bin/mysql -u root -p** and add password if want or proceed with no password and it will open mysql cli terminal in which you can do everything regarding RDBMS
Step 11 : Check all users details **SELECT User, Host, authentication_string FROM mysql.user;**
Step 12 : Create DataBase **CREATE DATABASE DATABASE_NAME;** >>  
Step 13 : To cross check run query **SHOW DATABASE;** and it will display all databases present
Step 14 : Run **pip3 install python-dotenv** and add .env file under **/settings/.env** and add required env variable like database details, version details, debug mode, admin details, API keys, also add FLASK_APP=main.py and then import dotenv and use environment variable in **/settings/config.py** file with all database related details like user, password, database name, port & host
Step 15 : If still not working with root password or password blank in user list then run query **UPDATE mysql.user SET authentication_string = PASSWORD('root') WHERE User = 'root'**;
Step 16 : Run query **FLUSH PRIVILEGES;**
Step 17 : **GRANT ALL PRIVILEGES ON DATABASE_NAME.* to root@localhost;**
Step 17 : **SHOW GRANTS FOR 'root'@'localhost';**
Step 18 : Still showing user related issue in mysql then run **ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';**
Step 19 : Now run migration.py by **python3 migration.py** it will create all tables to your databases automatically also alter table in my case student with **ALTER TABLE students ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;** and **ALTER TABLE students ADD COLUMN modified_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;** as we missed to add in migration file
Step 20 : **app.py** is for importing flask and CORS, cross_origin which is good for REST API
Step 21 : **main.py** is only using for delaring routing and calling API functions and return required responses in JSON format
Step 22 : **/v1/students.py** : All API functions under student class and we will simply importing this in main.py for routing the REST API as it will save a lot of our time in versioning.
Step 23 : Run **export FLASK_APP=main.py** and then **flask run** it will give you host in which you run your API in most of the cases it will be like **http://127.0.0.1:5000/**
Step 23 : Open Postmaster and add below API Urls
  **(1) POST : {url}/v1/student/insert**
      JSON Raw Body : 	
        {
          "roll_no":"R001",
          "first_name":"Ram",
          "last_name":"kumar",
          "class":"C#",
          "age":"24",
          "address":"India",
          "phone":"2322343123",
          "whatsapp": "2322343123"
        }
    **(2) GET : {URL}/v1/student/list**
    **(3) PUT : {URL}/v1/student/update**
      JSON Raw Body : 
        	{
            "id":"1",
            "roll_no":"R001",
            "first_name":"Newton",
            "last_name":"kumar",
            "class":"python",
            "age":"27",
            "address":"Delhi India",
            "phone" : "2322343123",
            "whatsapp" : "2322343123",
            "status" : "1"
          }
    **(4) GET : {URL}/v1/student/<int:student_id>** 
      To list details of a particular student
    **(5) DELETE : {URL}/v1/student/delete/<int:student_id>** 
      To Delete record from the database table for a particular student id
Step 24 : Check details in table by **select * from students;**

Some important commands : 
sudo pip3 install mysql-connector-python
pip3 install mysql-connector-python
sudo apt install python-pip
pip3 install flask
pip3 install flask-mysql
pip3 install -U flask-cors
pip3 show flask
pip3 install python-dotenv
source venv/bin/activate
pip3 freeze > requirements.txt
python3 -m venv mmapi_env 
. mmapi_env/bin/activate **To be run before any operation start for API

