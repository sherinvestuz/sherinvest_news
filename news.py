import os
import requests

TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
CHAT=os.getenv("TELEGRAM_CHAT_ID")

text="""🚨 SHERINVEST NEWS (TEST)

Bot muvaffaqiyatli ishladi.
Keyingi bosqichda real Reuters/SEC/FDA/Nasdaq filtri ulanadi.
#SherInvest"""

if TOKEN and CHAT:
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  json={"chat_id":CHAT,"text":text})
else:
    print("Secrets kiritilmagan.")
