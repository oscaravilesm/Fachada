from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def root():
    return "Pagina principal"

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id": user_id, "name": "test", "telefono": "981-169-5728"}

    # Obtener query param
    query = request.args.get("query")
    if query:
        user["query"] = query  # Corregido

    return jsonify(user), 200

@app.route('/users', methods=["POST"])
def create_user():
    data = request.get_json()
    data["status"] = "user created"
    return jsonify(data), 201

if __name__ == '__main__':  # ← CORREGIDO
    app.run(debug=True)
