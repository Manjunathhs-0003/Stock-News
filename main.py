import os
import requests
from twilio.rest import Client


STOCK_API_KEY = os.getenv("STOCK_API_KEY") # Add your stock API key in double quotes
NEWS_API_KEY = os.getenv("NEWS_API_KEY") # Add your news API key in double quotes
TWILIO_SID = os.getenv("TWILIO_SID") # Add your Twilio Account SID in double quotes
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN") # Add your Twilio authentication token here in double quotes

if not all([STOCK_API_KEY, NEWS_API_KEY, TWILIO_SID, TWILIO_AUTH_TOKEN]):
    raise ValueError("Please set all required environment variables.")

# Your stock and company details
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Parameters for stock API
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# Get stock data
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data["4. close"]
print(yesterdays_closing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterdays_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / float(yesterdays_closing_price)) * 100)
print(diff_percent)

# Get news if stock price changed significantly
if abs(diff_percent) > 5: #here the difference can be changed according to your needs
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Send articles via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in articles[:3]:
        message_body = f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        message = client.messages.create(
            body=message_body,
            from_='Enter the virtual twilio mobile number',
            to='Enter the mobile number you wnat to receive the news to (eg., +911234567890)'
        )
