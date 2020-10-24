import os

import requests
from flask import Flask, send_file, Response, redirect
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    host = 'https://hidden-journey-62459.herokuapp.com'
    path = '/piglatinize/'
    request_url = host + path

    text = get_fact()
    data = {"input_text": text}

    response = requests.post(request_url, data=data, allow_redirects=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    new_path = soup.find('a').text
    response_url = host + new_path

    return response_url

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

