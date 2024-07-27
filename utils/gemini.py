import google.generativeai as genai
def generate_answer(api,question, context):
    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        f"Answer the question '{question}' based on the context: {context}. dont write based on context in answer"
    )
    return response.text