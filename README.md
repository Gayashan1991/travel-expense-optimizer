Here’s a comprehensive `README.md` file tailored for your GitHub repository. This will guide users through setting up, running, and understanding your project.

---

# Travel Expense Refiner

The **Travel Expense Refiner** is an AI-powered Python-based tool that helps you plan your travel budget by integrating with multiple APIs to optimize travel expenses. It calculates the costs for flights, accommodation, transport, and more based on user input and provides a budget summary.

## Features

- Calculates flight prices using the **Skyscanner API**.
- Fetches accommodation details from **Booking.com API**.
- Estimates local transport costs with **Google Maps Distance Matrix API**.
- Converts currencies using **ExchangeRate-API**.
- Compares total expenses with your defined travel budget.
- Supports JSON-based user input for easy configuration.

## Project Structure

```
/project
    /data
        user_input.json              # User input JSON file (with travel details, budget, etc.)
    /apis
        travel_expense_refiner.py    # Main Python file (handles API integrations, calculations, and logic)
    /notebooks
        travel_expense_refiner.ipynb # Jupyter notebook for testing and running the backend
    /requirements.txt               # List of dependencies (requests, etc.)
    README.md                       # Project description and setup instructions
```

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.7 or above
- API keys for:
  - **Skyscanner API** (for flight data)
  - **Booking.com API** (for accommodation data)
  - **Google Maps API** (for transport data)
  - **ExchangeRate-API** (for currency conversion)

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Gayashan1991/travel-expense-optimizer.git
   cd travel-expense-optimizer
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain API keys:**
   - For **Skyscanner API**, sign up [here](https://partners.api.skyscanner.net).
   - For **Booking.com API**, sign up [here](https://www.booking.com).
   - For **Google Maps API**, sign up [here](https://console.developers.google.com/apis).
   - For **ExchangeRate-API**, sign up [here](https://www.exchangerate-api.com).

5. **Add your API keys** to the Python script or the Jupyter notebook.

   Edit `travel_expense_refiner.py` and replace the following placeholders with your keys:
   ```python
   flight_api_key = "YOUR_SKYSCANNER_API_KEY"
   hotel_api_key = "YOUR_BOOKING_COM_API_KEY"
   google_maps_api_key = "YOUR_GOOGLE_MAPS_API_KEY"
   exchange_rate_api_key = "YOUR_EXCHANGERATE_API_KEY"
   ```

6. **Prepare user input:**
   - Edit the `data/user_input.json` file to specify your destination, dates, group size, and budget details.
   - Example of the `user_input.json` format can be found in the repository.

7. **Run the code:**
   - **Option 1:** Run the Python script directly:
     ```bash
     python apis/travel_expense_refiner.py
     ```

   - **Option 2:** Alternatively, run the Jupyter notebook for an interactive experience:
     ```bash
     jupyter notebook notebooks/travel_expense_refiner.ipynb
     ```

## Example Input (JSON Format)

```json
{
    "destination": "Paris",
    "travel_dates": {"start": "2025-06-01", "end": "2025-06-10"},
    "group_size": 2,
    "total_budget": 3000,
    "category_budgets": {
        "flights": 1000,
        "accommodation": 1000,
        "food": 300,
        "activities": 500
    },
    "accommodation_type": "hotel",
    "transport_mode": "flight",
    "food_budget_per_day": 50,
    "activities": ["museums", "sightseeing", "local tours"],
    "currency": "USD",
    "exchange_rate": 1.1,
    "flexible_dates": true,
    "emergency_fund": 200
}
```

## Dependencies

The project relies on the following Python libraries:

- `requests` (for API calls)
- `json` (for loading and processing user input)

Install them by running:
```bash
pip install -r requirements.txt
```

## API Integrations

- **Skyscanner API**: Used to fetch flight data.
- **Booking.com API**: Used to fetch accommodation options and pricing.
- **Google Maps API**: Used to estimate transport costs.
- **ExchangeRate-API**: Used for currency conversion.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.
