from hyperliquid.exchange import Exchange
from hyperliquid.info import Info
import utils
import time

_, _, base_url = utils.get_config()
info = Info(base_url=base_url, skip_ws=False)

def callback(msg):
    if msg.get("channel") == "l2Book":
        data = msg["data"]
        bids = data["levels"][0][:3]
        asks = data["levels"][1][:3]
        print(f"BTC | Best bid: {bids[0]['px']} | Best ask: {asks[0]['px']}")
    else:
        print("Other message:", msg)

info.subscribe({"type": "l2Book", "coin": "BTC"}, callback)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down...")
    info.disconnect()