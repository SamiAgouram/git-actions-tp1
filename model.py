def predict_sentiment(text):

    """
    Analyse le texte et retourne un sentiment :
    - 'positive' si le texte contient 'happy' ou 'good'
    - 'negative' si le texte contient 'sad' ou 'bad'
    -  sinon 'neutral' 
    """

    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"