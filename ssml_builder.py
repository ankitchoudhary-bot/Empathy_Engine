def build_ssml(text, prosody, emotion):
    pause = "<break time='400ms'/>"

    if emotion == "concern":
        text = text.replace(".", f". {pause}")
    elif emotion == "joy":
        text = text.replace("!", "! <emphasis level='moderate'/>")

    ssml = f"""
<speak>
  <prosody rate="{prosody['rate']}"
           pitch="{prosody['pitch']}"
           volume="{prosody['volume']}">
    {text}
  </prosody>
</speak>
"""
    return ssml.strip()
