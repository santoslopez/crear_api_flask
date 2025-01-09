### Este codigo proviene de: https://www.youtube.com/watch?v=b0ZrmhyyCY4

from flask import Flask, jsonify, request,render_template
app = Flask(__name__)

@app.route('/')
def root():
    return "hello"

'''
GET - Obtener informacion
POST - Crear informacion
PUT - Actualizar informacion
DELETE - Borrar informacion
'''

@app.route("/users/<user_id>")
def get_user(user_id):

    user = {"id": user_id, "name": "Juan","telefono": "1234567890"}


    # argumento query
    # valor query_test
    # /users/2654?query=query_test

    # http://127.0.0.1:5000/users/eva?query=hola

    query = request.args.get("query")

    if query:
        user["query"] = query
    return jsonify(user), 200        


@app.route('/users',methods=['POST'])
def create_user():
    data = request.get_json()

    data["status"] = "user created"

    # indica que ya se creo
    return jsonify(data),201


if __name__ == '__main__':
    app.run(debug=True)
