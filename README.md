# Speech Transcription App 🎙️📝  

This is a **cross-platform** speech recording and transcription application built using:  
- **Frontend:** React Native (Expo)  
- **Backend:** Flask (Python)  
- **Speech Recognition:** OpenAI's Whisper  
- **Audio Processing:** FFmpeg  

This application **records system audio**, transcribes speech to text using **Whisper**, and stores transcriptions locally.  

---

## **Features 🚀**  
✅ Record **system audio** in real-time  
✅ Stop and save the recording  
✅ Transcribe the recorded audio into **text**  
✅ Store transcriptions **locally** in a text file  

---

## **Getting Started** 🛠️  

### **1. Prerequisites**  
Ensure you have the following installed:  
- **Node.js** (for React Native)  
- **Python 3.9+** (for the Flask backend)  
- **FFmpeg** (for system audio recording)  
- **Expo CLI** (for running the frontend)  

---

## **Backend Setup (Flask + Whisper) 🖥️**  

1️⃣ **Clone the repository:**  

git clone https://github.com/Manimaran-M3/SpeechTranscriptionApp.git
cd SpeechTranscriptionApp/backend

2️⃣ **Create a virtual environment & activate it:**

python -m venv venv
source venv/Scripts/activate  # On Windows

3️⃣ **Install dependencies:**

pip install -r requirements.txt

4️⃣ **Run the Flask backend:**

python backend.py

 The backend will start on http://127.0.0.1:5000

## **Frontend Setup (React Native + Expo) 📱** 

1️⃣ **Navigate to the frontend directory:**

cd ../frontend

2️⃣** Install dependencies:**

npm install

3️⃣ **Run the app in Expo:**

npm start

4️⃣ **Open the app on your phone using Expo Go OR in a web browser:**

npm run web
