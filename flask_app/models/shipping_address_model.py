from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class shipping_address:
    db="castleProject"
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']        
        self.street_address=data['street_address']
        self.city=data['city']
        self.state=data['state']
        self.zip=data['zip']

    @classmethod
    def get_one(cls,data):
        query="select * from shipping_address where id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results)<1:
            return False
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
        query="insert into shipping_address (name,street_address,city,state,zip) values (%(name)s,%(street_address)s,%(city)s,%(state)s,%(zip)s)"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls,data):
        query="delete from shipping_address where id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query="select * from shipping_address;"
        results = connectToMySQL(cls.db).query_db(query)
        products = []
        for row in results:
            products.append(cls(row))
        return products
    
    @classmethod
    def update(cls,data):
        query="update shipping_address set name=%(name)s,street_address=%(street_address)s,city=%(city)s,state=%(state)s,zip=%(zip)s where id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)