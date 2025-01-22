""""""
import json

from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(
        """
        <h1>Flask App</h1>
        <p>Click <a href="/lights">here</a> to see the lights.</p>
        """
    )

@app.route('/lights')
def lights():
    return render_template_string(open('lights/index.html').read(), canvas=dict(width=1200, height=1200))

@app.route('/lights/index.js')
def lights_js():
    return open('lights/index.js', encoding='utf-8').read()

@app.route('/lights/data.json')
def lights_data():
    return open('lights/test_pattern.json', encoding='utf-8').read()

@app.route('/lights/convert', methods=['GET', 'POST'])
def convert():
    # Security note: Being able to pass in any arbitrary URL means that an end user could potentially use this endpoint to forward requests to any server.
    # This could be used to perform a DDoS attack or to scrape data from other websites.
    # You should add some form of rate limiting, caching, or other security measures to prevent abuse.
    # And perhaps URL query string sanitization.
    # And ensuring that the resulting URL is actually an image, etc.

    CELL_SIZE = 30

    data = request.data

    from lights.convert import conv

    json_data = json.loads(data)
    url = json_data['url']

    height = json_data.get('height', 1200) // CELL_SIZE
    width = json_data.get('width', 1200) // CELL_SIZE

    return jsonify(conv(url, height, width))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5041)
