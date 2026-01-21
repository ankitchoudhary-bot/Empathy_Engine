from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def detect_emotion(text):
    results = classifier(text)[0]
    top = max(results, key=lambda x: x["score"])

    label = top["label"]
    intensity = top["score"]

    if label == "joy":
        emotion = "joy"
    elif label == "anger":
        emotion = "anger"
    elif label in ["sadness", "fear"]:
        emotion = "concern"
    else:
        emotion = "neutral"

    return emotion, intensity
