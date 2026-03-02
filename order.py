from eth_account import Account
from hyperliquid.exchange import Exchange
from hyperliquid.info import Info
import utils

address, secret, base_url = utils.get_config()

# Create a wallet object from your private key
wallet = Account.from_key(secret)

# Correct: Exchange(wallet, base_url)
exchange = Exchange(wallet, base_url)
info = Info(base_url=base_url, skip_ws=True)

# Limit buy 0.01 BTC at current mid - 1%
mids = info.all_mids()
btc_mid = float(mids["BTC"])
limit_px = float(round(btc_mid * 0.99))  # Round to nearest whole dollar

order_result = exchange.order(
    "BTC",
    is_buy=True,
    sz=0.01,
    limit_px=limit_px,
    order_type={"limit": {"tif": "Gtc"}},
    reduce_only=False
)
print(order_result)