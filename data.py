from hyperliquid.info import Info
import utils

address, scrt, base_url = utils.get_config()
info = Info(base_url=base_url, skip_ws=True)

# User state
user_state = info.spot_user_state(address)
print(user_state)

# Mid prices
mids = info.all_mids()
print(mids)

# L2 book for BTC
l2_book = info.l2_snapshot("BTC")

bids = l2_book["levels"][0][:5]
asks = l2_book["levels"][1][:5]

print("Top 5 bids:", bids)
print("Top 5 asks:", asks)


