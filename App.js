// import React, { useEffect, useState } from "react";
// import { View, Text, Button } from "react-native";
// import axios from "axios";

// export default function App() {
//     const [message, setMessage] = useState("Connecting...");

//     const fetchData = async () => {
//         try {
//             const response = await axios.get("http://192.168.29.11:5000/test");  // Use backend IP
//             setMessage(response.data.message);
//         } catch (error) {
//             setMessage("Error connecting to backend");
//             console.error(error);
//         }
//     };

//     useEffect(() => {
//         fetchData();
//     }, []);

//     return (
//         <View style={{ flex: 1, justifyContent: "center", alignItems: "center" }}>
//             <Text>{message}</Text>
//             <Button title="Refresh" onPress={fetchData} />
//         </View>
//     );
// }




import React, { useState } from "react";
import { View, Text, Button, ActivityIndicator, ScrollView, Alert } from "react-native";
import axios from "axios";
import Toast from "react-native-toast-message";

const API_URL = "http://192.168.29.11:5000"; // Replace with your backend URL

export default function App() {
  const [isRecording, setIsRecording] = useState(false);
  const [transcription, setTranscription] = useState("");
  const [loading, setLoading] = useState(false);

  // 🎙 Start Recording
  const startRecording = async () => {
    try {
      const response = await axios.get(`${API_URL}/start`);
      if (response.status === 200) {
        setIsRecording(true);
        Toast.show({ type: "success", text1: "Recording started!" });
      }
    } catch (error) {
      Toast.show({ type: "error", text1: "Failed to start recording" });
    }
  };

  // ⏹ Stop Recording
  const stopRecording = async () => {
    try {
      const response = await axios.get(`${API_URL}/stop`);
      if (response.status === 200) {
        setIsRecording(false);
        Toast.show({ type: "success", text1: "Recording stopped!" });
      }
    } catch (error) {
      Toast.show({ type: "error", text1: "Failed to stop recording" });
    }
  };

  // 📝 Transcribe Audio
  const transcribeAudio = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_URL}/transcribe`);
      if (response.status === 200) {
        setTranscription(response.data.transcription);
        Toast.show({ type: "success", text1: "Transcription completed!" });
      }
    } catch (error) {
      Toast.show({ type: "error", text1: "Failed to transcribe" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={{ flex: 1, padding: 20, justifyContent: "center", alignItems: "center" }}>
      <Toast />
      <Text style={{ fontSize: 20, fontWeight: "bold", marginBottom: 20 }}>Speech Transcription App</Text>

      <Button title="🎙 Start Recording" onPress={startRecording} disabled={isRecording} />
      <Button title="⏹ Stop Recording" onPress={stopRecording} disabled={!isRecording} />
      <Button title="📝 Transcribe Audio" onPress={transcribeAudio} disabled={isRecording} />

      {loading && <ActivityIndicator size="large" color="blue" style={{ marginTop: 20 }} />}

      <ScrollView style={{ marginTop: 20, padding: 10, backgroundColor: "#f2f2f2", borderRadius: 10, width: "100%" }}>
        <Text style={{ fontSize: 16 }}>{transcription || "Transcription will appear here..."}</Text>
      </ScrollView>
    </View>
  );
}
