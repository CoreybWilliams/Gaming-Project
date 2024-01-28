from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Products:
    db="castleProject"
    def __init__(self,data):
        self.id=data['id']
        self.name_of_product=data['name_of_product']        
        self.price=data['price']

    @classmethod
    def get_one(cls,data):
        query="select * from products where id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results)<1:
            return False
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
        query="insert into products (name_of_product,price) values (%(name_of_product)s,%(price)s)"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete(cls,data):
        query="delete from products where id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query="select * from products;"
        results = connectToMySQL(cls.db).query_db(query)
        products = []
        for row in results:
            products.append(cls(row))
        return products
    
# Manually set products
all_products_data = [
    {'id': 1, 'name_of_product': 'Lost Caverns of ixalan Commander Deck', 'price': 44.99},
    {'id': 2, 'name_of_product': 'Wilds of Eldraine Booster Pack', 'price': 4.99},
    {'id': 3, 'name_of_product': 'Phyrexia Bundle', 'price': 59.99},
    {'id': 4, 'name_of_product': 'Crimson Vow Booster Box', 'price': 109.99},
    {'id': 5, 'name_of_product': 'Pokemon 1st Editon Booster Pack', 'price': 399.99},
    {'id': 6, 'name_of_product': 'Scarlet and Violet Booster Pack', 'price': 4.99},
    {'id': 7, 'name_of_product': 'Obsidian Flames Booster Pac', 'price': 4.99},
    {'id': 8, 'name_of_product': 'Pandoras Rift Gift Set', 'price': 19.99},
    {'id': 9, 'name_of_product': 'Monarch Booster Pack', 'price': 4.99},
    {'id': 10, 'name_of_product': 'History Pack 1 Booster Pack', 'price': 4.99},
    {'id': 11, 'name_of_product': 'Prism Blitz Deck', 'price': 19.99},
    {'id': 12, 'name_of_product': 'Outsiders Booster Box', 'price': 54.99},
    {'id': 13, 'name_of_product': 'Battle of Omni Booster Pack', 'price': 4.99},
    {'id': 14, 'name_of_product': 'DCG Starter Deck', 'price': 9.99},
    {'id': 15, 'name_of_product': 'New Evolution Booster Box', 'price': 49.99},
    {'id': 16, 'name_of_product': 'DCG Gift Box', 'price': 24.99},
    {'id': 17, 'name_of_product': "Dungeon Master's Guide Book", 'price': 24.99},
    {'id': 18, 'name_of_product': "Players Hand Book", 'price': 24.99},
    {'id': 19, 'name_of_product': "Set of 7 Dice: Blue", 'price': 7.99},
    {'id': 20, 'name_of_product': 'Ancient Red Dragon Miniature', 'price': 49.99},
    {'id': 21, 'name_of_product': 'Exploding Kittens', 'price': 19.99},
    {'id': 22, 'name_of_product': 'Clue', 'price': 19.99},
    {'id': 23, 'name_of_product': 'Monopoly', 'price': 19.99},
    {'id': 24, 'name_of_product': 'Guess Who?', 'price': 19.99},
]

# Add products to the database
for product_data in all_products_data:
    product = Products(product_data)
    product.save(product.__dict__)