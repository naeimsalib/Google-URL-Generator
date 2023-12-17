from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "8057fe4b31mshd0baed97211d457p188f88jsnaf6f9d2012f7"  # Replace with your RapidAPI key
API_HOST = "google-url-generator.p.rapidapi.com"  # Replace with your RapidAPI host

@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    if request.method == 'POST':
        search_query = request.form.get('search_query')

        headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': API_HOST
        }

        api_url = f"https://{API_HOST}/generate-search-url/{search_query}"
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            url = response.json().get('search_url')  # Assuming the API returns JSON with 'search_url'

    return render_template('index.html', url=url)

if __name__ == '__main__':
    app.run(debug=True)
