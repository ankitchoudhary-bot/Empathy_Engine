# 🧠 Empathy Engine v2

Empathy Engine v2 is a **human-centric conversational AI system** that detects **granular emotions**
and generates **emotion-aware speech** using SSML-based prosody control.

This project upgrades traditional sentiment analysis into **emotional intelligence**.

---

## ✨ Key Features

- 🎭 Granular emotion detection (Joy, Anger, Concern, Neutral)
- 🧠 Transformer-based emotion classification
- 🎙️ Emotion → prosody mapping grounded in human voice psychology
- 🗣️ SSML generation with pauses, emphasis, and pacing
- 🌐 FastAPI backend with interactive Web UI

---

## 🎯 Supported Emotions

| Emotion   | Meaning |
|----------|--------|
| Joy | Excitement, enthusiasm |
| Anger | Frustration, dissatisfaction |
| Concern | Empathy, worry, reassurance |
| Neutral | Informational tone |

---

## 🧠 Emotion Detection Model

**Model:**  
`j-hartmann/emotion-english-distilroberta-base`

Detected labels are mapped as:

- joy → Joy
- anger → Anger
- sadness + fear → Concern
- others → Neutral

---

## 🎙️ Emotion → Voice Mapping

| Emotion | Rate | Pitch | Volume | SSML Behavior |
|------|------|------|------|------|
| Joy | Fast | Higher | Loud | Emphasis |
| Anger | Firm | Slightly High | X-Loud | Assertive |
| Concern | Slow | Lower | Soft | Pauses |
| Neutral | Normal | Neutral | Medium | None |

---

## 🌐 Architecture

    User Text
    ↓
    Emotion Detection (HF Transformer)
    ↓
    Emotion Mapping
    ↓
    Prosody Control
    ↓
    SSML Generation
    ↓
    TTS (Pluggable)


---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload


Open:
http://127.0.0.1:8000