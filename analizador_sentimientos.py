from transformers import pipeline

# Se carga una sola vez (correcto)
clasificador = pipeline(
    "sentiment-analysis",
    model="finiteautomata/beto-sentiment-analysis"
)

def analizar_sentimientos(texto: str):
    return clasificador(texto)