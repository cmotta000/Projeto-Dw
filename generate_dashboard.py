import jwt
import time

# URL e segredo do Metabase
METABASE_SITE_URL = "http://localhost:3000"
METABASE_SECRET_KEY = "8dfb049e27b99114f0b7a6ade89cec94dc288ae643a64bd1cf5446844132bd14"

# ID da pergunta do Metabase
QUESTION_ID = 51

# Gerar token JWT válido por 10 minutos
payload = {
    "resource": {"question": QUESTION_ID},
    "params": {},
    "exp": round(time.time()) + (60 * 10)
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

# URL de embed do iframe
iframeUrl = f"{METABASE_SITE_URL}/embed/question/{token}#bordered=true&titled=true"

# Gerar arquivo HTML
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Dashboard Metabase</title>
</head>
<body>
    <h1>Gráfico Metabase</h1>
    <iframe src="{iframeUrl}" frameborder="0" width="1000" height="600" allowtransparency></iframe>
</body>
</html>
"""

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ dashboard.html gerado com sucesso!")
print("Abra o arquivo no navegador para ver o gráfico.")