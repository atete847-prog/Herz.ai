from fastapi import FastAPI
from analizador_sentimientos import analizar_sentimientos

app = FastAPI()

@app.get("/sentimiento")
def sentimiento(texto: str):
    return analizar_sentimientos(texto)