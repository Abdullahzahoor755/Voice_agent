# ~/voice_agent/main.py

from voice.stt import listen
from voice.tts import speak
from brain.gemini_agent import ask, reset_chat

EXIT_WORDS = ["exit", "quit", "band karo", "bye", "khuda hafiz", "baند کرو"]

def get_input(use_voice=True):
    """Voice ya text — dono se input lo"""
    if use_voice:
        text = listen()
        if text:
            return text
    # voice fail ho ya empty ho toh text fallback
    try:
        text = input("Type karo (ya Enter for voice): ").strip()
        return text
    except (KeyboardInterrupt, EOFError):
        return "exit"

def main():
    print("=" * 50)
    print("   Voice AI Agent — Phase 1")
    print("   Urdu/English dono mein baat karo")
    print("   'exit' ya 'band karo' se band karo")
    print("=" * 50)

    speak("Assalam o Alaikum! Main aapka AI agent hun. Kya kaam hai?")

    use_voice = True

    while True:
        user_input = get_input(use_voice)

        if not user_input:
            continue

        # Exit check
        if any(word in user_input.lower() for word in EXIT_WORDS):
            speak("Khuda Hafiz! Allah Hafiz.")
            break

        # Voice toggle
        if "text mode" in user_input.lower():
            use_voice = False
            speak("Theek hai, ab text mode mein hun.")
            continue

        if "voice mode" in user_input.lower():
            use_voice = True
            speak("Theek hai, ab voice mode mein hun.")
            continue

        # Chat reset
        if "naya conversation" in user_input.lower() or "reset" in user_input.lower():
            reset_chat()
            speak("Conversation reset ho gayi. Naya shuru karte hain.")
            continue

        # Gemini se jawab lo
        print("Soch raha hun...")
        reply = ask(user_input)
        speak(reply)

if __name__ == "__main__":
    main()