# import the function that will return an instance of a connection
import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


# model the class after the friend table from our database
class Superhero:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password=data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# Now we use class methods to query our database
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        if len(user['fname']) < 2:
            flash("First Name must be at least 2 characters long.", "register")
            is_valid = False
        if len(user['lname']) < 2:
            flash("Last Name must be at least 2 characters long.", "register")
            is_valid = False
        if user['pw'] != user['cpw']:
            flash("Your password does not match the password confirmed", "register")
            is_valid = False
        return is_valid
    @staticmethod
    def validate_login( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "login")
            is_valid = False
        if len(user['pw']) < 1:
            flash("Please enter a password.", "login")
            is_valid = False
        return is_valid
    @classmethod
    def login(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        user = connectToMySQL('recipes_schema').query_db(query,data)
        if len(user) <1:
            flash("The email provided does not belong to any of our users. Please register", "login")
            return False
        print(user)
        return user[0]
    @classmethod
    def get_user_info(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        user = connectToMySQL('recipes_schema').query_db(query,data)
        return user[0]
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s ,%(password)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('recipes_schema').query_db( query, data )
