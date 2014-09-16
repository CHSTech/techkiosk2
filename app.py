from flask import Flask, Response, stream_with_context, render_template

import requests

app = Flask(__name__)

@app.route('/')
def kiosk():
    return render_template('kiosk.html')

@app.route('/mifi_data_usage')
def mifi_data_usage():
    req = requests.get('http://my.jetpack/datausage/info/', stream = True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

if __name__ == '__main__':
    app.run(debug=True, port=8000)
