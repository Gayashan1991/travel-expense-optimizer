import json
import os

def load_user_input(file_path):
    """Load user input from a JSON file."""
    try:
        with open(file_path, "r") as file:
            user_input = json.load(file)
        return user_input
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading user input: {e}")
        return None

import requests

# Function to get flight data from Skyscanner
def get_flight_data(origin, destination, start_date, api_key):
    url = f"https://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/US/USD/en-US/{origin}/{destination}/{start_date}"
    params = {'apiKey': api_key}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching flight data: {e}")
        return None

# Function to get accommodation data from Booking.com API via RapidAPI
def get_accommodation_data(destination, check_in_date, check_out_date, api_key):
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
    headers = {
        "X-RapidAPI-Host": "booking-com.p.rapidapi.com",
        "X-RapidAPI-Key": api_key
    }
    params = {
        "locale": "en-gb",
        "destination": destination,
        "checkin_date": check_in_date,
        "checkout_date": check_out_date,
        "adults": 2  # Default to group_size of 2 for now
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching accommodation data: {e}")
        return None

# Function to get transport data (e.g., from Google Maps Distance Matrix API)
def get_transport_data(origin, destination, transport_mode, api_key):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "mode": transport_mode,
        "key": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transport data: {e}")
        return None

# Function to convert currency using ExchangeRate-API
def convert_currency(amount, from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rate = data["conversion_rates"].get(to_currency)
        if rate:
            return amount * rate
        else:
            print(f"Error: Conversion rate for {to_currency} not found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching currency conversion data: {e}")
        return None


def calculate_travel_expenses(user_input, flight_api_key, hotel_api_key, google_maps_api_key, exchange_rate_api_key):
    destination = user_input["destination"]
    travel_dates = user_input["travel_dates"]
    start_date = travel_dates["start"]
    end_date = travel_dates["end"]
    group_size = user_input["group_size"]
    total_budget = user_input["total_budget"]
    accommodation_type = user_input["accommodation_type"]
    transport_mode = user_input["transport_mode"]
    
    # Get flight data
    flight_data = get_flight_data("SFO", destination, start_date, flight_api_key)  # Assuming origin is "SFO"
    if flight_data:
        flight_price = flight_data["Quotes"][0]["MinPrice"] * group_size  # Assuming the first quote
        print(f"Flight Price for {group_size} people: {flight_price} USD")
    
    # Get accommodation data
    accommodation_data = get_accommodation_data(destination, start_date, end_date, hotel_api_key)
    if accommodation_data:
        accommodation_price = accommodation_data["result"][0]["price"] * group_size  # Assume first result
        print(f"Accommodation Price for {group_size} people: {accommodation_price} USD")
    
    # Get local transport data
    transport_data = get_transport_data("SFO", destination, transport_mode, google_maps_api_key)
    if transport_data:
        transport_cost = transport_data["rows"][0]["elements"][0]["duration"]["value"]  # Example cost estimation
        print(f"Estimated transport cost: {transport_cost} USD")

    # Convert currency if necessary
    converted_budget = convert_currency(total_budget, user_input["currency"], "USD", exchange_rate_api_key)
    if converted_budget:
        print(f"Total Budget (converted to USD): {converted_budget} USD")

    # Calculate total expenses and compare with the user's budget
    total_expenses = flight_price + accommodation_price + transport_cost
    print(f"\nTotal Expenses: {total_expenses} USD")
    if total_expenses <= total_budget:
        print("The travel plan is within the budget!")
    else:
        print("The travel plan exceeds the budget!")


if __name__ == "__main__":
    # Define the API keys
    flight_api_key = "YOUR_SKYSCANNER_API_KEY"
    hotel_api_key = "YOUR_BOOKING_COM_API_KEY"
    google_maps_api_key = "YOUR_GOOGLE_MAPS_API_KEY"
    exchange_rate_api_key = "YOUR_EXCHANGERATE_API_KEY"

    # Load user input
    user_input_file_path = os.path.join("data", "user_input.json")
    user_input = load_user_input(user_input_file_path)

    if user_input:
        calculate_travel_expenses(user_input, flight_api_key, hotel_api_key, google_maps_api_key, exchange_rate_api_key)
