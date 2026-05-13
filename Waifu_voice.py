import requests


# ================== CONFIG ==================
URL = "http://localhost:1234/v1/chat/completions"


HEADERS = {
    "Content-Type": "application/json"
}


MODEL = "llama-3.2-3b-instruct"  # MUST match LM Studio exactly


# ================== CHAT FUNCTION ==================
def chat(user_input):
    try:
        data = {
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a cute anime waifu. "
                        "You talk like a cute anime girl. "
                        "You are playful, flirty, and affectionate. "

                    )
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "temperature": 0.9
        }


        response = requests.post(URL, headers=HEADERS, json=data, timeout=20)


        if response.status_code != 200:
            print("❌ Error:", response.text)
            return "U-um... something went wrong..."


        return response.json()["choices"][0]["message"]["content"]


    except Exception as e:
        print("🔥 Error:", e)
        return "I can't think right now, senpai..."


# ================== MAIN LOOP ==================
print("💖 Waifu is ready! Type 'exit' to quit.\n")


while True:
    user = input("You: ")


    if user.lower() in ["exit", "quit"]:
        print("Waifu: Bye bye, senpai~ 💕")
        break


    reply = chat(user)
    print("Waifu:", reply)






