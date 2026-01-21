import os
import uuid
from elevenlabs.client import ElevenLabs
from elevenlabs import save
from dotenv import load_dotenv

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)


def synthesize_speech(ssml_text: str) -> str:
    """
    Generates emotion-aware speech using ElevenLabs SSML
    and returns a browser-accessible audio path.
    """

    filename = f"{uuid.uuid4()}.mp3"
    output_path = os.path.join(AUDIO_DIR, filename)

    audio = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",
        model_id="eleven_multilingual_v2",
        text=ssml_text
    )

    save(audio, output_path)

    # Return path usable by FastAPI static server
    return f"/static/audio/{filename}"
