from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "orders-service"}), 200


@app.route("/orders", methods=["GET"])
def orders():
    return jsonify(
        {
            "orders": [
                {"id": 101, "status": "created"},
                {"id": 102, "status": "shipped"}
            ]
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
