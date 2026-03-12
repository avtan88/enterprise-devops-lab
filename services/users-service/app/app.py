from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "users-service"}), 200


@app.route("/users", methods=["GET"])
def users():
    return jsonify(
        {
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ]
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
