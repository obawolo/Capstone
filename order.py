import requests, json
import alpaca_trade_api as tradeapi
#pip3 install alpaca_trade_api  
#in termial or cmd

API_KEY = "PKW1E9L1XPP0QSN07Q2L" 
SECRET_KEY = "mfx6Rf4kNWicVNgW35eiKg4JtXxnNiq5cMRFz4z6"
#keys are linked to my account, you can make your own account or I can give you the password 
#https://app.alpaca.markets/paper/dashboard/overview 
#Username: yl1025@scarletmail.rutgers.edu 
#Password: CAPTSONE1234

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDRERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}



def get_account():
    r = reqiests.get(ACCOUNT_URL, headers= HEADERS)

    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }

    r =requests.post(ORDRERS_URL, json = data, headers=HEADERS)
    return json.loads(r.content)


response = create_order("SPY", 100, "sell", "market", "gtc")
#                                   "sell"

print(response)
