<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Stock News</h1>

<h2>Overview</h2>
<p>This Python project fetches stock data and news articles related to a specified company and sends SMS alerts via Twilio when there is a significant change in the stock price. It utilizes APIs from Alpha Vantage for stock data, News API for news articles, and Twilio for SMS messaging.</p>

<h2>Features</h2>
<ul>
    <li>Fetches daily stock data from Alpha Vantage API.</li>
    <li>Retrieves news articles related to the specified company from News API.</li>
    <li>Sends SMS alerts via Twilio when the stock price change exceeds a specified threshold.</li>
    <li>Utilizes environment variables for API keys and endpoints for enhanced security.</li>
</ul>

<h2>How the Project Works</h2>
<ol>
    <li>Retrieves daily stock data for a specified company using the Alpha Vantage API.</li>
    <li>Calculates the percentage difference in the stock price between two consecutive trading days.</li>
    <li>If the percentage difference exceeds a specified threshold (e.g., 5%), fetches news articles related to the company using the News API.</li>
    <li>Sends SMS alerts via Twilio with the headline and brief description of the top news articles.</li>
</ol>

<h2>Installation Guide</h2>
<h3>Clone the Repository</h3>
<pre><code>git clone https://github.com/Manjunathhs-0003/Stock-News
cd Stock-News
</code></pre>

<h2>Usage</h2>
<ol>
    <li>Set up environment variables for the required API keys and endpoints.</li>
    <li>Run the Python script <code>main.py</code>.</li>
    <pre><code>python main.py</code></pre>
</ol>

<h2>APIs Used</h2>
<ul>
    <li><strong>Alpha Vantage</strong>:
        <ul>
            <li>Endpoint: <a href="https://www.alphavantage.co/">Alpha Vantage</a></li>
            <li>Documentation: Navigate to the Alpha Vantage website, sign up for an account, and obtain the API key from the dashboard or API section.</li>
        </ul>
    </li>
    <li><strong>News API</strong>:
        <ul>
            <li>Endpoint: <a href="https://newsapi.org/">News API</a></li>
            <li>Documentation: Visit the News API website, sign up for an account or log in, and obtain the API key from the dashboard or API section.</li>
        </ul>
    </li>
    <li><strong>Twilio</strong>:
        <ul>
            <li>Endpoint: <a href="https://www.twilio.com/">Twilio</a></li>
            <li>Documentation: Go to the Twilio website, sign up for an account, obtain the Account SID and Auth Token from the dashboard, and set up a virtual phone number.</li>
        </ul>
    </li>
</ul>

</body>
</html>
