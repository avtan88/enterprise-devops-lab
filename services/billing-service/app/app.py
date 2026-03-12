from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "billing-service"}), 200


@app.route("/billing", methods=["GET"])
def billing():
    return jsonify(
        {
            "billing": [
                {"invoice": "INV-1001", "amount": 250},
                {"invoice": "INV-1002", "amount": 400}
            ]
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
