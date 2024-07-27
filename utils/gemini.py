import google.generativeai as genai
import os

def generate_answer(question, context):
    genai.configure(api_key=os.getenv("key"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        f"Answer the question '{question}' based on the context: {context}. dont write based on context in answer"
    )
    return response.text