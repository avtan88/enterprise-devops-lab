from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "inventory-service"}), 200


@app.route("/inventory", methods=["GET"])
def inventory():
    return jsonify(
        {
            "items": [
                {"sku": "A-100", "stock": 15},
                {"sku": "B-200", "stock": 8}
            ]
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
