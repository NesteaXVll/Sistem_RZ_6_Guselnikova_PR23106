from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
        1: {
            "name": "Anastasia",
            "age": 20
        },
        2: {
            "name": "Irina",
            "age": 19
        },
        3: {
            "name": "Elizaveta",
            "age": 20
        }
    }

@app.route('/users/', methods=['GET'])
def returnUserInfo():
    id = request.args.get("id")
    pass
    id = int(id)
    user_info = users.get(id)
    return jsonify(user_info)

if __name__ == "__main__":
    app.run(debug=True)