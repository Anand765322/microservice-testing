from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"}), 200

@app.route("/api/data", methods=["POST"])
def data():
    req_data = request.get_json()
    return jsonify({"received": req_data}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
