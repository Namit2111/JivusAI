from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
from utils.gemini import generate_answer

app = Flask(__name__)

# Function to extract text from the product website
def extract_text_from_website(url):
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                           'Accept-Language': 'en-US, en;q=0.5'})
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # soup = BeautifulSoup(response.content, "lxml")
    # print(soup.get_text())
    return soup.get_text()

# Function to process questions and generate answers
def process_questions(questions, product_url):
    answers = []
    website_text = extract_text_from_website(product_url)
    for question in questions:
        answer = generate_answer(question, website_text)
        answers.append((question, answer))
    return answers

# Route for the web UI
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_url = request.form['product_url']
        questions = request.form['questions'].splitlines()
        answers = process_questions(questions, product_url)
        return render_template('answers.html', answers=answers)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
