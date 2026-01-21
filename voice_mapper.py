def emotion_to_ssml_params(emotion, intensity):
    scale = min(intensity, 1.0)

    if emotion == "joy":
        return {
            "rate": f"{115 + int(25 * scale)}%",
            "pitch": f"+{4 + int(3 * scale)}st",
            "volume": "loud"
        }

    elif emotion == "anger":
        return {
            "rate": f"{105 + int(10 * scale)}%",
            "pitch": f"+{1 + int(2 * scale)}st",
            "volume": "x-loud"
        }

    elif emotion == "concern":
        return {
            "rate": f"{85 - int(10 * scale)}%",
            "pitch": f"-{2 + int(1 * scale)}st",
            "volume": "soft"
        }

    else:
        return {
            "rate": "100%",
            "pitch": "0st",
            "volume": "medium"
        }
