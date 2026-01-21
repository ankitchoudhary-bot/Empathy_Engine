from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from emotion_detector import detect_emotion
from voice_mapper import emotion_to_ssml_params
from ssml_builder import build_ssml
from elevenlabs_tts import synthesize_speech

app = FastAPI(title="Empathy Engine")

# Serve audio files
app.mount("/static", StaticFiles(directory="static"), name="static")


class TextInput(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def ui():
    return """
    <html>
    <head>
        <title>Empathy Engine</title>
        <style>
            body { font-family: Arial; padding: 40px; background: #f4f6f8; }
            textarea { width: 100%; height: 120px; font-size: 16px; }
            button { padding: 10px 20px; margin-top: 10px; }
            audio { margin-top: 15px; width: 100%; }
        </style>
    </head>
    <body>
        <h2>🧠 Empathy Engine</h2>
        <textarea id="text"></textarea><br/>
        <button onclick="speak()">Generate Speech</button>

        <p><b>Emotion:</b> <span id="emotion"></span></p>
        <p><b>Intensity:</b> <span id="intensity"></span></p>

        <audio id="audio" controls></audio>

        <script>
            async function speak() {
                const text = document.getElementById("text").value;

                const response = await fetch("/speak", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ text })
                });

                const data = await response.json();

                document.getElementById("emotion").innerText = data.emotion;
                document.getElementById("intensity").innerText = data.intensity;

                const audio = document.getElementById("audio");
                audio.src = data.audio_file;
                audio.load();
                audio.play();
            }
        </script>
    </body>
    </html>
    """


@app.post("/speak")
def speak(payload: TextInput):
    text = payload.text.strip()

    emotion, intensity = detect_emotion(text)
    prosody = emotion_to_ssml_params(emotion, intensity)
    ssml = build_ssml(text, prosody, emotion)
    audio_path = synthesize_speech(ssml)

    return {
        "emotion": emotion,
        "intensity": round(float(intensity), 2),
        "audio_file": audio_path
    }
