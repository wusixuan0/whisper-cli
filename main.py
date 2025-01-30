from src.whisper_client import WhisperTranscriber
import os
from dotenv import load_dotenv
import sys
import sounddevice as sd
from scipy.io import wavfile
import time
from pathlib import Path

def main():
    load_dotenv()
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

    if (not OPENAI_API_KEY):
        print("Please set your OPENAI_API_KEY in a .env file")
        sys.exit(1)

    transcriber = WhisperTranscriber(OPENAI_API_KEY)

    try:
        print("Recording... (Press Enter to stop, Ctrl+C to cancel)")

        fs = 16000  # Sample rate

        # Start recording AND start our timer
        start_time = time.time()
        recording = sd.rec(int(fs * 60 * 10), samplerate=fs, channels=1)

        # Wait for Enter key
        input()

        # Stop recording
        sd.stop()

        # Calculate how long we actually recorded
        duration = time.time() - start_time
        samples_to_keep = int(fs * duration)  # Convert seconds to samples

        # Trim the recording to actual duration
        trimmed_recording = recording[:samples_to_keep]

        # Save trimmed recording
        recordings_dir = Path("temp/recordings")
        recordings_dir.mkdir(parents=True, exist_ok=True)
        audio_file_path = recordings_dir / "recording.wav"
        wavfile.write(audio_file_path, fs, trimmed_recording)

        print(f"Recorded {duration:.2f} seconds. Transcribing...")

        transcription = transcriber.transcribe(audio_file_path)
        print(transcription)

    except KeyboardInterrupt:
        print("\nRecording cancelled")
        sys.exit(0)

if __name__ == "__main__":
    main()