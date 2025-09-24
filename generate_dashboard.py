# generate_dashboard.py
# Requer: pip install PyJWT
import jwt
import time
import html

METABASE_SITE_URL = "http://localhost:3000"
METABASE_SECRET_KEY = "cbc3835d29d5c0750fcf9eee6ca49796a8bca699aca1001021ac47cecb31072e"

# ID da pergunta/metabase question que você quer embutir
QUESTION_ID = 38

# tempo de expiração em segundos (10 minutos)
EXPIRATION_SECONDS = 60 * 10

payload = {
    "resource": {"question": QUESTION_ID},
    "params": {},
    "exp": round(time.time()) + EXPIRATION_SECONDS
}

# Gera o token JWT
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

# Dependendo da versão do PyJWT, jwt.encode retorna bytes ou str
if isinstance(token, bytes):
    token = token.decode("utf-8")

iframe_url = f"{METABASE_SITE_URL}/embed/question/{token}#bordered=true&titled=true"

# Monta o HTML
html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Metabase Embed - Question {QUESTION_ID}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 20px; }}
    .info {{ margin-bottom: 12px; color: #333; }}
    iframe {{ border: 1px solid #ddd; width: 100%; height: 800px; }}
  </style>
</head>
<body>
  <h1>Embed Metabase - Question {QUESTION_ID}</h1>
  <p class="info">Token válido por {EXPIRATION_SECONDS//60} minutos. Se expirar, rode este script novamente.</p>
  <p class="info"><strong>URL usada no iframe (copiar/colar):</strong><br />
  <code>{html.escape(iframe_url)}</code></p>
  <iframe src="{html.escape(iframe_url)}" frameborder="0" allowtransparency></iframe>
</body>
</html>
"""

# Escreve o arquivo dashboard.html
out_path = "dashboard.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ dashboard.html gerado com sucesso em:", out_path)
print("Abra o arquivo no navegador (duplo clique) ou cole a URL abaixo no navegador:")
print(iframe_url)