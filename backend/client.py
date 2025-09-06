import requests
import json_output_parser as jsp
def url_maker(dep_code, dep_date, arrival_loc, num_adults):
    return f"http://127.0.0.1:5001/flights?origin={dep_code}&destination={arrival_loc}&departure_date={dep_date}&adults={num_adults}"

def get_requests():
    while True:
        date = input("Enter date of flight in YYYY-MM-DD or Q to quit:ap ")
        if date == "Q":
            break
        dep_code = input("Enter departure code: ")
        location = input("Enter arrival code: ")
        number_of_adults = int(input("Enter number of adults: "))
        url = url_maker(dep_code, date, location, number_of_adults)
        response = requests.get(url)
        print(response.json())
        print(jsp.extract_features(response.json()))

if __name__ == "__main__":
    get_requests()