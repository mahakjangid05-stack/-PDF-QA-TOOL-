
from fastapi import FastAPI
app = FastAPI()

response = {
    "hello": "yes i am you chatbot name is mayank",
    "kya hai": "mai tera chatbot hu",
    "name": "tu beta apna name bata"
}

@app.post("/chat/")
def chat(message: str):
    user_message = message.lower()
    if user_message in response:
        reply = response[user_message]  # ✅ FIX
    else:
        reply = "muje nhi pata"
    return {"reply": reply}  # ✅ FIX

