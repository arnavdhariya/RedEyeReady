import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")

TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_OFFERS_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"

# Airports allowed
ORIGIN_AIRPORTS = ["OAK", "SJC", "SFO"]

def get_access_token():
    data = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_API_SECRET
    }
    response = requests.post(TOKEN_URL, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

@app.route("/flights", methods=["GET"])
def search_flights():
    origin = request.args.get("origin")
    destination = request.args.get("destination")
    departure_date = request.args.get("departure_date")
    adults = request.args.get("adults", "1")

    if not origin or not destination or not departure_date:
        return jsonify({"error": "origin, destination, and departure_date are required"}), 400

    if origin.upper() not in ORIGIN_AIRPORTS:
        return jsonify({"error": f"Only flights from {ORIGIN_AIRPORTS} are allowed"}), 400

    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}

    params = {
        "originLocationCode": origin.upper(),
        "destinationLocationCode": destination.upper(),
        "departureDate": departure_date,
        "adults": adults,
        "max": 10
    }

    response = requests.get(FLIGHT_OFFERS_URL, headers=headers, params=params)
    if response.status_code != 200:
        return jsonify({"error": response.json()}), response.status_code

    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
