from hyperliquid.exchange import Exchange, Info
import utils
import time

_, _, base_url = utils.get_config()
info = Info(base_url=base_url, skip_ws=False)

def callback(msg):
    print("Update message:", msg)

info.subscribe({"type": "l2_book", "coin": "BTC"}, callback)
time.sleep(10)  # Keep the subscription alive for 10 seconds``