from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# API Key
API_KEY = "ded01c9-8b1e-4c3a-9f1e-2b5a6c7d8e9f"

# -----------------------------------
# Helper function
# -----------------------------------

def validate_api_key():

    api_key = request.headers.get("x-api-key")

    if api_key != API_KEY:
        return False

    return True

# -----------------------------------
# Sales Endpoint
# -----------------------------------

@app.route("/sales", methods=["GET"])
def get_sales():

    # Validate API Key
    if not validate_api_key():
        return jsonify({
            "error": "Invalid API Key"
        }), 401

    # Read sales CSV
    df = pd.read_csv("data/mindx_raw_sales_data.csv")

    # Convert to JSON
    # Replace NaN with None
    df = df.replace({np.nan: None})

    data = df.to_dict(orient="records")

    return jsonify(data)

# -----------------------------------
# Exchange Rate Endpoint
# -----------------------------------

@app.route("/exchange-rate", methods=["GET"])
def get_exchange_rates():

    # Validate API Key
    if not validate_api_key():
        return jsonify({
            "error": "Invalid API Key"
        }), 401

    # Read exchange rate CSV
    df = pd.read_csv("data/exchange_rate_2425.csv")

    # Convert to JSON
    df = df.replace({np.nan: None})

    data = df.to_dict(orient="records")

    return jsonify(data)

# -----------------------------------
# Run app
# -----------------------------------

if __name__ == "__main__":
    app.run(debug=True)
