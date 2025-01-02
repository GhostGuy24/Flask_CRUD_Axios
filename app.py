from flask import Flask, render_template, request

products = [
    {"id": 1, "desc": "Running Shoes", "price": 59.99},
    {"id": 2, "desc": "Basketball Shoes", "price": 89.99},
    {"id": 3, "desc": "Casual Sneakers", "price": 49.99},
    {"id": 4, "desc": "Formal Leather Shoes", "price": 129.99},
    {"id": 5, "desc": "Hiking Boots", "price": 99.99}
]
app = Flask(__name__)

#CRUD
#R - read
@app.route("/")
def prods():
    return render_template('index.html',my_products=products) 

#C - create 
@app.route("/add",  methods=['GET', 'POST'])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else: #POST
        data = request.get_json()
        price= data.get('price')
        desc= data.get('desc')
    products.append({"id": len(products)+1, "price": price,"desc":desc},)
    return render_template("index.html",my_products=products)

#D - delete
@app.route("/del/<id>" ,methods=['GET', 'DELETE'])
def delete_product(id=0):
    product_to_remove = next((product for product in products if product["id"] == int(id)), None)
    if product_to_remove: products.remove(product_to_remove)
    return render_template("index.html",my_products=products)
# U - update
@app.route("/upd/<id>" ,methods=['GET',"PUT"])
def upd_product(id=0):
    product_to_update= next((product for product in products if product["id"] == int(id)), None)
    data = request.get_json()
    price= data.get('price')
    desc= data.get('desc')
    if product_to_update:
        product_to_update["price"] =price
        product_to_update["desc"] =desc
    return render_template("index.html",my_products=products)


