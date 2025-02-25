"""
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with the backend

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Backend is working!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
"""



from flask import Flask, jsonify
import os
import subprocess
import whisper
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

OUTPUT_FILE = "record.wav"
DEVICE_NAME = "Stereo Mix (Realtek(R) Audio)"
WHISPER_MODEL = "medium"
recording_process = None
recording_active = False

@app.route("/start", methods=["GET"])
def start_recording():
    global recording_process, recording_active
    if recording_active:
        return jsonify({"message": "Recording is already in progress!"}), 400

    command = f'ffmpeg -f dshow -i audio="{DEVICE_NAME}" "{OUTPUT_FILE}"'
    recording_process = subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
    recording_active = True
    return jsonify({"message": "Recording started"}), 200

@app.route("/stop", methods=["GET"])
def stop_recording():
    global recording_process, recording_active
    if recording_process and recording_active:
        os.system("taskkill /F /IM ffmpeg.exe")
        recording_process = None
        recording_active = False
        return jsonify({"message": "Recording stopped"}), 200
    return jsonify({"message": "No active recording to stop"}), 400

@app.route("/transcribe", methods=["GET"])
def transcribe_audio():
    if recording_active:
        return jsonify({"message": "Stop the recording before transcribing!"}), 400

    if os.path.exists(OUTPUT_FILE):
        model = whisper.load_model(WHISPER_MODEL)
        result = model.transcribe(OUTPUT_FILE)
        transcription = result["text"]

        now = datetime.now()
        timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")

        with open("Transcribed_data.txt", "a", encoding="utf-8") as file:
            file.write(f"{timestamp} {transcription}\n\n")

        return jsonify({"message": "Transcription completed", "transcription": transcription}), 200
    return jsonify({"message": "No recording found"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
