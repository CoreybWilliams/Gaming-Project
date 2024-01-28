from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db="castleproject"
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']        
        self.email=data['email']
        self.password=data['password']

    # @classmethod
    # def get_all(cls):
    #     query="select * from users;"
    #     results = connectToMySQL(cls.db).query_db(query)
    #     users = []
    #     for row in results:
    #         users.append(cls(row))
    #     return users
    
    @classmethod
    def get_one(cls,data):
        query="select * from users where id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results)<1:
            return False
        return cls(results[0])

    @classmethod
    def get_email(cls,data):
        query="SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results)<1:
            return False
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
        query="insert into users (name,email,password) values (%(name)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    # @classmethod
    # def update(cls,data):
    #     query="update users set name=%(name)s,email=%(email)s, password=%(password)s where id=%(id)s;"
    #     return connectToMySQL(cls.db).query_db(query, data)

    # @classmethod
    # def delete(cls,data):
    #     query="delete from users where id = %(id)s;"
    #     return connectToMySQL(cls.db).query_db(query, data)
    
    # @staticmethod
    # def validate(user):
    #     is_valid = True
    #     query = 'SELECT * FROM users WHERE email = %(email)s;'
    #     results = connectToMySQL(User.db).query_db(query, user)
    #     # print(results,"THESE ARE THE RESULTS*******************")
    #     if len(results) >= 1:
    #         is_valid = False
    #         flash("Email is already in use in our database")
    #     if len(user['first_name']) < 2:
    #         is_valid = False
    #         flash("Please use least least 2 characters for the first Name")
    #     if len(user['last_name']) < 2:
    #         is_valid = False
    #         flash("Please use least least 2 characters for the last Name")
    #     if len(user['email']) < 2:
    #         is_valid = False
    #         flash("Please use proper email format for the email")
    #     if len(user['password']) < 4:
    #         is_valid = False
    #         flash("Please use least least 6 characters for the password")
    #     if user['password'] != user['confirm']:
    #         is_valid = False
    #         flash("Passwords don't match")
    #     return is_valid

    #     @staticmethod
    # def validate_card(user):
    #     is_valid = True
    #     query = 'SELECT * FROM users WHERE email = %(email)s;'
    #     results = connectToMySQL(User.db).query_db(query, user)
    #     # print(results,"THESE ARE THE RESULTS*******************")
    #     if len(results) >= 1:
    #         is_valid = False
    #         flash("Email is already in use in our database")
    #     if len(user['first_name']) < 2:
    #         is_valid = False
    #         flash("Please use least least 2 characters for the first Name")
    #     if len(user['last_name']) < 2:
    #         is_valid = False
    #         flash("Please use least least 2 characters for the last Name")
    #     if len(user['email']) < 2:
    #         is_valid = False
    #         flash("Please use proper email format for the email")
    #     if len(user['password']) < 4:
    #         is_valid = False
    #         flash("Please use least least 6 characters for the password")
    #     if user['password'] != user['confirm']:
    #         is_valid = False
    #         flash("Passwords don't match")
    #     return is_valid