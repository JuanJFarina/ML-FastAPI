from textblob import TextBlob
from deep_translator import GoogleTranslator

def test_sentiment_analysis() -> None:
    blob = TextBlob("I loved it")
    polarity = blob.sentiment.polarity    
    sentiment = "positivo" if polarity > 0 else "negativo" if polarity < 0 else "neutral"
    assert sentiment == "positivo"

def test_text_translation() -> None:
    textotrans = GoogleTranslator(source='auto', target='es').translate(text="My name is Juan")
    assert textotrans == "Mi nombre es Juan"

def test_analysis_spanish() -> None:
    textotrans = GoogleTranslator(source='auto', target='en').translate(text="Me encantó !")
    blob = TextBlob(textotrans)
    polarity = blob.sentiment.polarity
    sentiment = "positivo" if polarity > 0 else "negativo" if polarity < 0 else "neutral"
    assert sentiment == "positivo"

def test_analysis_french() -> None:
    textotrans = GoogleTranslator(source='auto', target='en').translate(text="Je aimé c'est musique !")
    blob = TextBlob(textotrans)
    polarity = blob.sentiment.polarity
    sentiment = "positivo" if polarity > 0 else "negativo" if polarity < 0 else "neutral"
    assert sentiment == "positivo"

def test_analysis_italian() -> None:
    textotrans = GoogleTranslator(source='auto', target='en').translate(text="Io detesto questo lugar")
    blob = TextBlob(textotrans)
    polarity = blob.sentiment.polarity
    sentiment = "positivo" if polarity > 0 else "negativo" if polarity < 0 else "neutral"
    assert sentiment == "negativo"
