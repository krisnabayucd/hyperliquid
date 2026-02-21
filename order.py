from hyperliquid.exchange import Exchange
from hyperliquid.info import Info
import utils

address, secret, base_url = utils.get_config()
exchange = Exchange(address, secret, base_url)

# Limit buy 0.01 BTC at current mid - 1%
mids = Info(base_url=base_url).all_mids()
btc_mid = float(mids["BTC"])
limit_px = btc_mid * 0.99

order = {
    "asset": "BTC",
    "is_buy": True,
    "reduce_only": False,
    "sz": 0.01,
    "limit_px": limit_px,
    "order_type": {"limit": {"tif": "Gtc"}}
}
result = exchange.order(**order)
print(result)