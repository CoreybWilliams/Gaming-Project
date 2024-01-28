from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Creditcard:
    db="castleProject"
    def __init__(self,data):
        self.id=data['id']
        self.name_on_card=data['name_on_card']        
        self.card_number=data['card_number']
        self.expiration_date=data['expiration_date']
        self.CVC=data['CVC']
    
    @staticmethod
    def validate_cc(cc):
        is_valid = True
        query = 'SELECT * FROM creditcard WHERE name_on_card = %(name_on_card)s;'
        results = connectToMySQL(Creditcard.db).query_db(query,cc)
        if len(cc['name_on_card']) < 2:
            flash("Please insert the name on your card.","cc")
            is_valid = False
        if len(cc['card_number']) < 15:
            flash("Please enter your 15 or 16 digit card number.","cc")
            is_valid = False
        if len(cc['expiration_date']) <7:
            flash("Expiration date doesn't match.","cc")
            is_valid = False
        if len(cc['CVC']) <4:
            flash("Please input the security code on the back of your card.","cc")
            is_valid = False
        return is_valid
    
    @classmethod
    def save_cc(cls,data):
        query="insert into creditcard (name_on_card,card_number,expiration_date,CVC) values (%(name_on_card)s,%(card_number)s,%(expiration_date)s,%(CVC)s)"
        return connectToMySQL(cls.db).query_db(query, data)

