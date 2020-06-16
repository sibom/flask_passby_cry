"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask,render_template,request
import internet_sock
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def hello():
    """Renders a sample page."""
    return "<html>  <a href=/get>GET</a> <br><a href=/post>POST</a><br><br><br><p>author:sibom</p></html>"

@app.route('/post')
def post():
    """Renders a sample page."""
    return render_template('POST.html')

@app.route('/post/result', methods=['POST'])
def post_result():
    """Renders a sample page."""
    r = request.form['name']
    texthtml = internet_sock.internet_post(r)
    return texthtml

@app.route('/get')
def get():
    """Renders a sample page."""
    return render_template('GET.html')


@app.route('/get/result')
def get_result():
    """Renders a sample page."""
    r = request.args.get('text')
    texthtml = internet_sock.internet_get(r)
    return texthtml

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
