"""Launches and renders routes for paced's resume page."""

import base64
import datetime
import hashlib
import os

import pyotp
from flask import redirect, render_template, request, send_from_directory
from utils import launchServer

# Necessary settings
DEBUG = False

if DEBUG:
    CSSFILES = [
    ]

    JSFILES = [
    ]
else:
    CSSFILES = JSFILES = []

app = launchServer(DEBUG, CSSFILES, JSFILES)


@app.context_processor
def inject_debug():
    """Inject debug state into every template."""
    return dict(debug=app.debug)


@app.errorhandler(404)
def notFound(e):
    """View for 404 page."""
    return render_template('content/notfound.jinja.html'), 404


@app.route('/', methods=['GET'])
def index():
    """Home page with basic TOTP explanation."""
    return render_template('content/index.jinja.html')


@app.route('/security/', methods=['GET'])
def security():
    """Security explanation page."""
    return render_template('content/security.jinja.html')


@app.route('/demo/', methods=['GET'])
def demo():
    """Demo page."""
    return render_template('content/demo.jinja.html')


@app.route('/api/status', methods=['GET'])
def status():
    """Simple API response to see if API is alive."""
    return "OK"


@app.route('/api/endpoint', methods=['GET'])
def endpoint():
    """API endpoint to generate a TOTP token."""
    try:
        secret = request.args["key"]
        interval = int(request.args["interval"])
        digits = int(request.args["length"])
        algo = request.args["algo"]

        secret = base64.b32encode(secret.encode())

        if algo == "hmac_sha1":
            digest = hashlib.sha1
        elif algo == "hmac_sha256":
            digest = hashlib.sha256
        elif algo == "hmac_sha512":
            digest = hashlib.sha512
        elif algo == "hmac_md5":
            digest = hashlib.md5
        else:
            raise Exception

        totp = pyotp.TOTP(secret, digits, digest, interval=interval)
        return totp.generate_otp(totp.timecode(datetime.datetime.now()))
    except Exception as e:
        return "NaN"


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Contact forms."""
    return send_from_directory('static/', 'sitemap.xml')


@app.route('/favicon.ico')
def favicon():
    """Favicon for IE-based browsers."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicons/favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/robots.txt')
def robots():
    """Robot file for SEO."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robots.txt')


if __name__ == "__main__":
    app.run(debug=DEBUG, host='0.0.0.0')
