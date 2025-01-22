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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5041)
