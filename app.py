""""""

from flask import Flask, jsonify, render_template_string

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
    return open('lights/index.html').read()

@app.route('/lights/index.js')
def lights_js():
    return open('lights/index.js', encoding='utf-8').read()

@app.route('/lights/data.json')
def lights_data():
    #return open('lights/data.json').read()
    from lights.convert import conv
    #data = conv('lights/Starry_Night.jpg')
    data = conv()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5041)
