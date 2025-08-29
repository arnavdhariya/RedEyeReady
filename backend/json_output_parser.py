import json

def get_data_from_json(data_original: str) -> dict:
    with open(data_original) as json_file:
        return json.load(json_file)

def extract_features(data: dict):
    flight_data = []

    for offer in data.get("data", []):
        price = get_price(offer)  # Price is tied to the offer

        for itinerary in offer.get("itineraries", []):
            for segment in itinerary.get("segments", []):
                dep_airport, dep_time = get_departure_time_airport(segment)
                arr_airport, arr_time = get_arrival_time_airport(segment)

                flight_data.append({
                    "airline": get_airline(segment),
                    "flight_number": get_flight_number(segment),
                    "departure_airport": dep_airport,
                    "departure_time": dep_time,
                    "arrival_airport": arr_airport,
                    "arrival_time": arr_time,
                    "duration": get_duration(segment),
                    "price": price
                })

    return flight_data

def get_airline(segment: dict) -> str:
    airline_content = segment.get('operating', {})
    return airline_content.get('carrierName')

def get_flight_number(segment: dict) -> str:
    return segment.get('number')

def get_departure_time_airport(segment: dict) -> tuple:
    dep = segment.get("departure", {})
    return dep.get("iataCode"), dep.get("at")

def get_arrival_time_airport(segment: dict) -> tuple:
    arr = segment.get("arrival", {})
    return arr.get("iataCode"), arr.get("at")

def get_duration(segment: dict) -> str:
    """duration is in ISO string format"""
    return segment.get("duration")

def get_price(offer: dict) -> str:
    price = offer.get("price", {})
    return price.get("total")
