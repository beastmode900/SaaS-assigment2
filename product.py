from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data structure for products
products = {
    1: {"name": "Apples", "price": 1.50, "quantity": 100},
    2: {"name": "Bananas", "price": 0.50, "quantity": 200},
}

# Endpoint to retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# Endpoint to retrieve a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404

# Endpoint to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()

    if not all(k in data for k in ("name", "price", "quantity")):
        return jsonify({"error": "Missing product data"}), 400

    new_id = max(products.keys()) + 1
    products[new_id] = {
        "name": data['name'],
        "price": data['price'],
        "quantity": data['quantity']
    }
    
    return jsonify({"message": "Product added", "product_id": new_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
