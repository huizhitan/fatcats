def api_function():
    import requests
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=8N288SMI711NV5VT'
    r = requests.get(url)
    data = r.json()

    return data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    