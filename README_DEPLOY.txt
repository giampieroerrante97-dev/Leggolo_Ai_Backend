RENDER – DEPLOY BACKEND LEGGOLO AI

1) Crea un nuovo repo su GitHub: Leggolo-AI-Backend
   - Carica server.py, requirements.txt, runtime.txt, README_DEPLOY.txt

2) Vai su https://dashboard.render.com  → New → Web Service
   - Connect repository: scegli Leggolo-AI-Backend
   - Name: leggolo-backend
   - Region: Frankfurt (EU)
   - Build Command: pip install -r requirements.txt
   - Start Command: python server.py

3) Clicca “Create Web Service”.
   Al termine avrai un URL tipo:
   https://leggolo-backend.onrender.com

4) Test rapidi:
   - /health       → GET
   - /exercise     → POST JSON { "subject":"matematica","level":"facile","language":"it","topic":"frazioni" }
   - /scan         → POST JSON { "task":"summary","text":"..."}  oppure { "task":"math","text":"(2+3)^2/5" }
