from flask import Flask, request
import requests

app = Flask(__name__)

def get_day():
    response = requests.get("https://nbu.uz/uz/exchange-rates/json/")
    data = response.json()[-1]
    return data["nbu_buy_price"]
usd = get_day()

@app.route('/api/to-usd', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    r = request.args
    date = float(r["amount"])
    return {"amount": date, "currency": "UZS", "converted": round(date/usd, 2), "convertedCurrency": "USD"}

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    r = request.args
    date = float(r["amount"])
    return {"amount": date, "currency": "USD", "converted": round(date*usd, 2), "convertedCurrency": "UZS"}
    

if __name__ == '__main__':
    app.run()    