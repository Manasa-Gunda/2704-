import openai
import speech_recognition as sr

openai.api_key = "xxx"
def get_voice_input():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio_data = r.record(source,duration=5)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print(text)
        
    return text


def get_response(input):
        response = openai.Completion.create(
            model = "gpt-3.5-turbo",
            prompt=input,max_tokens=150
        )
        return response['choice'][0]['text']
        


if __name__ == "__main__":
    print("chatbot: Hi user!! How may I help you?")
    user_input = get_voice_input()
    response = get_response(user_input)
    print(response)
            
