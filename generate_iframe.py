# generate_iframe.py
import jwt
import time

METABASE_SITE_URL = "http://localhost:3000"
METABASE_SECRET_KEY = "cbc3835d29d5c0750fcf9eee6ca49796a8bca699aca1001021ac47cecb31072e"

payload = {
    "resource": {"question": 51},
    "params": {},
    "exp": round(time.time()) + (60 * 10)  # expira em 10 min
}

token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
iframeUrl = METABASE_SITE_URL + "/embed/question/" + token + "#bordered=true&titled=true"

print("Acesse este link no navegador ou cole em um <iframe>:\n")
print(iframeUrl)