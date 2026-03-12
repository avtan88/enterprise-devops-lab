from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "catalog-service"}), 200


@app.route("/catalog", methods=["GET"])
def catalog():
    return jsonify(
        {
            "catalog": [
                {"sku": "CAT-100", "name": "Laptop"},
                {"sku": "CAT-200", "name": "Keyboard"}
            ]
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
