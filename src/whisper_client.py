from openai import OpenAI
from pathlib import Path

class WhisperTranscriber:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def transcribe(self, audio_file_path: Path, prompt: str = None) -> str:
        """Transcribe audio file using Whisper API"""

        audio_file = open(audio_file_path, "rb")
        params = {
            "model": "whisper-1",
            "file": audio_file,
        }
        if prompt:
            params["prompt"] = prompt

        transcription = self.client.audio.transcriptions.create(**params)
        return transcription.text