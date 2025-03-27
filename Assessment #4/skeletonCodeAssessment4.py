import random
from gtts import gTTS
import os

# Sample patient database with language, preferred communication channel, and age
patients = [
    {"id": 1, "name": "Ravi Kumar", "language": "Tamil", "channel": "SMS", "age": 65},
    {"id": 2, "name": "Ananya Rao", "language": "Telugu", "channel": "WhatsApp", "age": 30},
    {"id": 3, "name": "Joseph Mathew", "language": "Malayalam", "channel": "IVR", "age": 70},
    {"id": 4, "name": "Rahul Sharma", "language": "Hindi", "channel": "SMS", "age": 50},
    {"id": 5, "name": "David Thomas", "language": "English", "channel": "WhatsApp", "age": 25},
]

# Multi-language template management
messages = {
    "Tamil": ["உங்கள் நேரம் உறுதிசெய்யப்பட்டது. தயவுசெய்து வருக!", "உங்கள் சந்திப்பு நாளை. தயவுசெய்து உறுதிப்படுத்தவும்!"],
    "Telugu": ["మీ నియామకం నిర్ధారించబడింది. దయచేసి రండి!", "మీ సమావేశం రేపు ఉంది. దయచేసి నిర్ధారించండి!"],
    "Malayalam": ["നിങ്ങളുടെ അപോയിന്റ്മെന്റ് സ്ഥിരീകരിച്ചിരിക്കുന്നു. ദയവായി വരൂ!", "നാളെ നിങ്ങളുടെ യോഗം. ദയവായി സ്ഥിരീകരിക്കുക!"],
    "Hindi": ["आपका अपॉइंटमेंट कन्फर्म हो गया है। कृपया आएं!", "आपकी मुलाकात कल है। कृपया पुष्टि करें!"],
    "English": ["Your appointment is confirmed. Please visit!", "Your meeting is tomorrow. Please confirm!"]
}

wait_time_updates = {
    "Tamil": "உங்கள் காத்திருப்பு நேரம்: 15 நிமிடங்கள்",
    "Telugu": "మీ వెయిట్ టైం: 15 నిమిషాలు",
    "Malayalam": "നിങ്ങളുടെ കാത്തിരിപ്പ് സമയം: 15 മിനിറ്റ്",
    "Hindi": "आपका प्रतीक्षा समय: 15 मिनट",
    "English": "Your wait time: 15 minutes"
}

prescription_alerts = {
    "Tamil": "உங்கள் மருந்து மீளப்பார்வை தேவை!",
    "Telugu": "మీ మందుల పునఃసమీక్ష అవసరం!",
    "Malayalam": "നിങ്ങളുടെ ഔഷധ പുനഃപരിശോധന ആവശ്യമാണ്!",
    "Hindi": "आपकी दवा की समीक्षा आवश्यक है!",
    "English": "Your prescription review is needed!"
}

# Function to send messages with A/B Testing
def send_message(patient, message_type="Appointment Confirmation"):
    """Simulate sending a message based on patient language and preferred channel"""
    language = patient["language"]
    channel = patient["channel"]
    message = random.choice(messages.get(language, messages["English"]))  # A/B Testing
    
    if channel == "IVR":
        text_to_speech(message, language, patient["name"])
    else:
        print(f"📩 {message_type} via {channel} to {patient['name']} ({language}): {message}")

# Function to send wait time updates
def send_wait_time_update(patient):
    message = wait_time_updates.get(patient["language"], wait_time_updates["English"])
    send_message(patient, "Wait Time Update")

# Function to send prescription alerts
def send_prescription_alert(patient):
    message = prescription_alerts.get(patient["language"], prescription_alerts["English"])
    send_message(patient, "Prescription Alert")

# Function to generate voice messages for IVR
def text_to_speech(text, language, name):
    lang_map = {"Tamil": "ta", "Telugu": "te", "Malayalam": "ml", "Hindi": "hi", "English": "en"}
    tts = gTTS(text=text, lang=lang_map.get(language, "en"))
    filename = f"ivr_message_{name}.mp3"
    tts.save(filename)
    os.system(f"start {filename}")  # Plays the message
    print(f"📞 IVR Call Sent to {name} in {language}.")

# Function to collect patient feedback
def collect_feedback():
    """Simulates patient feedback collection"""
    feedback_responses = ["Very clear", "Somewhat clear", "Difficult to understand", "No response"]
    feedback_data = {patient["name"]: random.choice(feedback_responses) for patient in patients}
    print("\n📊 Patient Feedback Survey Results:")
    for name, feedback in feedback_data.items():
        print(f"🗣️ {name}: {feedback}")
    return feedback_data

# Send messages to all patients
for patient in patients:
    send_message(patient)
    send_wait_time_update(patient)
    send_prescription_alert(patient)

# Effectiveness measurement: track confirmations and satisfaction
def measure_effectiveness():
    """Simulates confirmation tracking and A/B testing"""
    confirmed = sum(random.choices([0, 1], k=len(patients)))  # Random confirmations
    confirmation_rate = (confirmed / len(patients)) * 100
    print(f"✅ Confirmation Rate: {confirmation_rate:.2f}%")

measure_effectiveness()
collect_feedback()
