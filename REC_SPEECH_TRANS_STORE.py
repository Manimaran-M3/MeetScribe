import os
import time
import subprocess
import keyboard
import whisper
from datetime import datetime

OUTPUT_FILE = "record.wav"
DEVICE_NAME = "Stereo Mix (Realtek(R) Audio)"  # Change this!
WHISPER_MODEL = "medium"  # Choose your Whisper model

recording_process = None
recording_active = False

def record_audio():
    global recording_process, recording_active
    if recording_active:
        print("⚠️ Recording is already in progress!")
        return

    command = f'ffmpeg -f dshow -i audio="{DEVICE_NAME}" "{OUTPUT_FILE}"'
    recording_process = subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
    recording_active = True
    print("▶️ Recording started. Press 's' to stop.")

def stop_recording():
    global recording_process, recording_active
    if recording_process and recording_active:
        print("⏹️ Stopping recording...")

        # **Force Kill FFmpeg using taskkill**
        os.system("taskkill /F /IM ffmpeg.exe")

        recording_process = None
        recording_active = False
        print("✅ Recording stopped.")
    else:
        print("⚠️ No active recording to stop.")

def transcribe_audio():
    if recording_active:
        print("⚠️ Stop the recording before transcribing!")
        return

    if os.path.exists(OUTPUT_FILE):
        print("📝 Transcribing with Whisper...")
        try:
            model = whisper.load_model(WHISPER_MODEL)
            result = model.transcribe(OUTPUT_FILE)
            transcription = result["text"]

            # Get the current date and time
            now = datetime.now()
            timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")  # Format: [YYYY-MM-DD HH:MM:SS]

            try:
                with open("Transcribed_data.txt", "a", encoding="utf-8") as file:
                    file.write(f"{timestamp} {transcription}\n\n")  # Add timestamp
                print("📜 Content added to the file with timestamp.")
            except Exception as f:
                print("❌ Error in file creation")
                print("TRANSCRIPTION:", transcription)
        except Exception as e:
            print(f"❌ Error during Whisper transcription: {e}")
    else:
        print("⚠️ No recording found for transcription.")

def main():
    print("🎤 Press 'r' to start recording, 's' to stop, 't' to transcribe, 'q' to exit.")

    while True:
        if keyboard.is_pressed('r') and not recording_active:
            record_audio()
            time.sleep(0.3)  # Debounce
        elif keyboard.is_pressed('s') and recording_active:
            stop_recording()
            time.sleep(0.3)  # Debounce
        elif keyboard.is_pressed('t') and not recording_active:
            transcribe_audio()
            time.sleep(0.3)  # Debounce
        elif keyboard.is_pressed('q'):
            print("👋 Exiting...")
            if recording_active:
                stop_recording()
            break
        time.sleep(0.05)  # Reduce CPU usage

if __name__ == "__main__":
    main()
