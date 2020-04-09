from flask import Flask, render_template, request, flash, redirect, session, jsonify
import requests
import os

app = Flask(__name__)
app.secret_key = 'FLATTEN THE CURVE'

API_KEY = os.environ['GIPHY_KEY']

@app.route('/')
def homepage():
    """Show homepage."""

    url = 'https://api.giphy.com/v1/gifs/search'
    payload = {'apikey': API_KEY,
               'q': 'coronavirus',
               'limit': 50,
               'offset': 20,
               'rating': 'R',
               'lang': 'en'}

    response = requests.get(url, params=payload)
    data = response.json()
    gifs = data['data']
    main = gifs[0]
    rest = gifs[1:]
        

    return render_template('homepage.html',
                           main=main,
                           gifs=rest)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')