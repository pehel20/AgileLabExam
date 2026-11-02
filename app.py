from flask import Flask, request, jsonify
from leave_system import leave_request

app = Flask(__name__)

@app.route("/leave", methods=["POST"])
def leave():
    data = request.get_json()
    result = leave_request(data["emp_id"], data["days"])
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
