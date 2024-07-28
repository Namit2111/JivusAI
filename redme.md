# Jivusai

Jivusai is a web application that uses the Gemini API to generate answers to questions based on the context of a product website.

## Getting Started

To get started with Jivusai, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/jivusai.git`
2. Create a Python virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`
5. Set up the environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add the following line to the `.env` file: `api=YOUR_API_KEY` (You can get api key form gemini api)
6. Run the application: `python app.py`

## Usage

To use Jivusai, navigate to `http://localhost:5000` in your web browser. Enter the URL of the product website and the questions you want to ask in the respective fields. Click the "Submit" button to generate the answers.

