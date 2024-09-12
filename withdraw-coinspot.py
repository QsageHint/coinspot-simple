from coinspot import FullAccessAPIV2
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    # Replace with your API key and secret
    API_KEY = os.environ.get("API_KEY")
    API_SECRET = os.environ.get("API_SECRET")

    # Withdraw details
    COIN_TYPE = 'BTC'          # Coin to withdraw, e.g., BTC, LTC, DOGE
    AMOUNT = 0             # Amount to withdraw
    ADDRESS = 'bc1qs697u8r2wfj094vgu5x0rjeyu6hvr9x9ru7h8g'  # The receiving address
    EMAIL_CONFIRM = 'NO'       # Whether to require email confirmation, 'YES' or 'NO'
    NETWORK = None             # Optional, e.g., 'BNB', 'ETH'
    PAYMENT_ID = None          # Optional, only for coins requiring a payment ID

    FullAccessAPI = FullAccessAPIV2(api_key=API_KEY, api_secret=API_SECRET)

    # Call the withdrawal function
    result = FullAccessAPI.coin_withdrawal(coin=COIN_TYPE, amount=AMOUNT, address=ADDRESS, require_email_confirmation=EMAIL_CONFIRM, network=NETWORK, payment_id=PAYMENT_ID)
    # result = FullAccessAPI.get_coin_withdrawal_details(coin=COIN_TYPE)

    print(result)  # Display the result of the withdrawal request .0v  