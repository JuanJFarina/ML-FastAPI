from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from textblob import TextBlob
from langdetect import detect
from deep_translator import GoogleTranslator
from pydantic import BaseModel

description = """
Welcome to the Translation and Sentiment Analysis API!

This API allows you to translate text from any language to Spanish and also analyze sentiment in any language, so you can know if a comment is either positive, neutral or negative.

For using our services endpoints you'll have to provide your API KEY as a query parameter, in this manner:

POST /analyze?api_key=apikey

"""

app = FastAPI(
    title="Challenge App",
    description=description,
    summary="Translation and Sentiment Analysis App"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    texto: str

class TranslateRequest(BaseModel):
    texto: str

api_keys = {
    "key123": "user",
    "adminkey456": "admin"
}

def api_key_query(api_key: str = ''):
    if api_key:
        return api_key
    else:
        raise HTTPException(status_code=400, detail="API key required")

def get_api_key(api_key: str = Depends(api_key_query)):
    if api_key in api_keys:
        return api_key
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.get("/")
def read_root():
    """
    Simple API usage message.

    Example:

    {
        "mensaje": "text",
        "analizar": "text",
        "traducir": "text"
    }
    """
    return {
        "mensaje": "API de traducción al español y análisis de sentimiento de textos en cualquier idioma",
        "analizar": "Usar /analyze?texto para recibir una respuesta positiva, negativa o neutral sobre el sentimiento del autor, sin importar el idioma",
        "traducir": "Usar /translate?texto para recibir una respuesta traducida al español"
    }

@app.post("/analyze")
def analyze_sentiment(
    analyze_request: AnalyzeRequest,
    api_key: str = Depends(get_api_key)
):
    """
    Analyze the sentiment of the given text.

    Args:
        analyze_request (AnalyzeRequest): The request containing the text to analyze.

        Example:

        {
            "texto": "Me encantó !"
        }

    Returns:
        dict: The sentiment analysis result.

        Example:

        {
            "sentimiento": "positivo",
            "polaridad": 0.875
        }
    """
    try:
        textotrans = GoogleTranslator(source='auto', target='en').translate(text=analyze_request.texto)

        blob = TextBlob(textotrans)

        polarity = blob.sentiment.polarity
        
        sentiment = "positivo" if polarity > 0 else "negativo" if polarity < 0 else "neutral"
        
        return {"sentimiento": sentiment, "polaridad": polarity}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/translate")
def translate_text(
    translate_request: TranslateRequest,
    api_key: str = Depends(get_api_key)
):
    """
    Translate the given text to Spanish.

    Args:
        translate_request (TranslateRequest): The request containing the text to translate.

        {
            "texto": "Hello ! How are you ?"
        }

    Returns:
        dict: The translated text.

        {
            "traducción": "Hola ! Cómo estás ?"
        }
    """
    try:
        origLang = detect(translate_request.texto)
        textotrans = GoogleTranslator(source='auto', target='es').translate(text=translate_request.texto)

        return {
            "traduccion": textotrans,
            "idioma_original": origLang
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))