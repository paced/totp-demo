"""Utilities for the main manage.py file."""

from flask import Flask
from flask_compressor import Compressor, CSSBundle, FileAsset, JSBundle
from flask_htmlmin import HTMLMIN as htmlmin


def launchServer(debug, cssFiles, jsFiles):
    """Create Flask server object given static file reference lists."""
    app = Flask(__name__)
    app.config.from_object(__name__)

    # Do we do HTML minification?
    app.config['MINIFY_PAGE'] = not debug
    htmlmin(app)

    # Compress static assets by creating bundles from static objects.
    compressor = Compressor(app)
    allCSS = list()
    allJS = list()

    for i in cssFiles:
        allCSS.append(FileAsset(filename=i, processors=['cssmin']))

    cssBundle = CSSBundle('allCSS', assets=allCSS, processors=['cssmin'])
    compressor.register_bundle(cssBundle)

    for i in jsFiles:
        allJS.append(FileAsset(filename=i, processors=['jsmin']))

    jsBundle = JSBundle('allJS', assets=allJS, processors=['jsmin'])
    compressor.register_bundle(jsBundle)

    return app
