# generate_iframe.py
import jwt
import time

METABASE_SITE_URL = "http://localhost:3000"
METABASE_SECRET_KEY = "8dfb049e27b99114f0b7a6ade89cec94dc288ae643a64bd1cf5446844132bd14"

payload = {
    "resource": {"question": 51},
    "params": {},
    "exp": round(time.time()) + (60 * 10)  # expira em 10 min
}

token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
iframeUrl = METABASE_SITE_URL + "/embed/question/" + token + "#bordered=true&titled=true"

print("Acesse este link no navegador ou cole em um <iframe>:\n")
print(iframeUrl)