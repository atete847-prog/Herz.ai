from transformers import pipeline

MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"

analizador = pipeline("sentiment-analysis", model=MODEL_NAME)

def analizar_sentimientos(texto: str):
    resultado = analizador(texto)
    return {"texto": texto, "resultado": resultado}