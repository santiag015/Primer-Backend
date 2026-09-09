from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
 {"id": 1, "nombre": "Laptop", "precio": 1200},
 {"id": 2, "nombre": "Mouse", "precio": 25},
 {"id": 3, "nombre": "Teclado", "precio": 75}
]

@app.route('/')
def home():
    return "welcome to the flask API!"

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
 return jsonify(productos), 200


@app.route('/api/productos/<int:id>', methods=['GET'])
def get_producto(id):
   producto = next((p for p in productos if p["id"]== id),None)
   if productos:
      return jsonify(producto)
   else:
      return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/api/productos', methods=['POST'])
def add_producto():
   if not request.is_json:
      return jsonify({"error": "solicitud debe ser JSON"}), 400
   else:
      if not request.get_json().get("nombre") or not request.get_json().get("precio"):
         return jsonify({"Error": "Faltan campos requeridos"}), 400
      else:
         nuevo_producto = request.get_json()
         productos.append(nuevo_producto)
         return jsonify(nuevo_producto), 201

@app.route('/api/productos/<int:id>', methods=['PUT'])
def update_producto(id):
   producto = next((p for p in productos if p["id"]==id), None)
   if producto:
      data = request.get_json()
      producto.update(data)
      return jsonify(producto)
   else:
      return jsonify({"Error": "Producto no encontrado"}), 404

@app.route('/api/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
   producto = next((p for p in productos if p["id"]==id), None)
   if producto:
      productos.remove(producto)
      return jsonify({"message": "Producto eliminado"})
   else:
      return jsonify({"Error": "Producto no encontrado"}), 404
   

if __name__ == '__main__':
    app.run(debug=True)