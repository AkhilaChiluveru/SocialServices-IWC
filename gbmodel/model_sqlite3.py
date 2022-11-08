"""
Social Service Events In Portland  flask app.
SQLite database that looks something like the following:

+-----------------+----------------+------------------------+--------------+----------+--------+-------------------------------------------------------+-----------------+
| name            | Location       | Type of Service        |Phone Number  |Hours Of Operation |  Review                                               |    Actions      |
+=================+======================+==================+========================+=================================================================+=================+
| Old-age Home    |  2020 NE       |Helping needy old       |503-224-0409  |9am-9pm            |  You have helped 100's aged people with food,medicine |  Update,Delete  |
+-----------------+----------------+------------------------+--------------+-------------------+-------------------------------------------------------+-----------------+

This can be created with the following SQL (see bottom of this file):
CREATE TABLE  social_service (name_of_service_organization TEXT,  type_of_service TEXT, location TEXT,operating_hours DATETIME,phone_number TEXT, review TEXT);

"""

from ast import Param
from .Model import Model
import sqlite3
DB_FILE = 'services.db'    # file for our Database

CREATE_TABLE_SOCIALSERVICE = """
CREATE TABLE IF NOT EXISTS social_service
(id NUMBER NOT NULL,
name_of_service_organization TEXT, 
type_of_service TEXT,
location TEXT,
phone_number VARCHAR(12), 
operating_hours DATETIME,
review TEXT,
PRIMARY KEY (id)) """

GET_ALL_SERVICES = "SELECT * FROM social_Service"

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from social_service")
        except sqlite3.OperationalError:
            cursor.execute(CREATE_TABLE_SOCIALSERVICE)
        cursor.close()
    
    def select(self):
        """
        Gets all rows from the database
        Each row contains: name_of_service_organization, type_of_service, location, operating_hours, phone_number, review
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        return cursor.execute(GET_ALL_SERVICES).fetchall()

    def insert(self,id,name_of_service_organization, type_of_service, location,phone_number, operating_hours,  review):
        
        """
        Inserts entry into database
        :param id: number Not null
        :param Name: String
        :param Street_Address: String
        :Param Type_Of_Service: string
        :Param Phone_Number varchar(12)
        :Param Hours_Of_Operation datetime
        :Param reviews string 
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'id':id,'name': name_of_service_organization, 'type': type_of_service,
                  'location': location,  'phone_number': phone_number, 'hours': operating_hours,'review': review}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO social_service (id,name_of_service_organization ,type_of_service , location ,phone_number ,operating_hours ,review ) 
        VALUES (:id,:name,:type,:location,:phone_number,:hours,:review)""" , params)
        connection.commit()
        cursor.close()
        return True

    def delete(self,id):
         params= {'id':id}
         connection = sqlite3.connect(DB_FILE)
         cursor = connection.cursor()
         cursor.execute("""DELETE FROM social_service  WHERE id= :id""",params)
         connection.commit()
         cursor.close()
         return True

    def update(self,id,name_of_service_organization,  location,phone_number, operating_hours,  review):
        
        """
        Updates values of that entry based on id value
        :param id: number
        :param Name: String
        :param Street_Address: String
        :Param Type_Of_Service: string
        :Param Phone_Number varchar(50)
        :Param Hours_Of_Operation datetime
        :Param reviews string 
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'id':id,'name': name_of_service_organization, 
                  'location': location,  'phone_number': phone_number, 'hours': operating_hours,'review': review}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("""UPDATE social_service set name_of_service_organization=:name , location=:location ,phone_number=:phone_number ,operating_hours=:hours ,review=:review 
        WHERE id=:id""" , params)
        connection.commit()
        cursor.close()
        return True

    def selectById(self,id):
        """
        Gets one row from the database based on id
        :param id :number
        :return: 1 row with name_of_service_organization, type_of_service, location, operating_hours, phone_number, review values
        """
        params ={'id':id}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        return cursor.execute("""SELECT * FROM social_service WHERE id=:id""",params).fetchone()
