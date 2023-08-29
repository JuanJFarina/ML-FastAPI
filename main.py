from fastapi import FastAPI, HTTPException
from textblob import TextBlob
from deep_translator import GoogleTranslator

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "mensaje": "API de traducción al español y análisis de sentimiento de textos en cualquier idioma",
        "analizar": "Usar /analyze?texto para recibir una respuesta positiva, negativa o neutral sobre el sentimiento del autor, sin importar el idioma",
        "traducir": "Usar /translate?texto para recibir una respuesta traducida al español"
    }

@app.post("/analyze")
def analyze_sentiment(texto: str):
    try:
        textotrans = GoogleTranslator(source='auto', target='en').translate(text=texto)

        blob = TextBlob(textotrans)

        polarity = blob.sentiment.polarity
        
        sentiment = "positivo" if polarity > 0 else "negativo" if polarity < 0 else "neutral"
        
        return {"sentimiento": sentiment, "polaridad": polarity}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/translate")
def analyze_sentiment(texto: str):
    try:
        textotrans = GoogleTranslator(source='auto', target='es').translate(text=texto)

        return {
            "traducción": textotrans
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))