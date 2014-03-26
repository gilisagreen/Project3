""" main.py is the top level script.

Return "Hello World" at the root URL.
"""

import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template
app = Flask(__name__.split('.')[0])


@app.route('/')
def memory(name=None):
  """ Return hello template at application root URL."""
  return render_template('welcome.html')


@app.route('/oneplayer')
def oneplayer(name=None):
  return render_template('oneplayer.html')

@app.route('/twoplayer')
def twoplayer(name=None):
  return render_template('twoplayer.html')

@app.route('/cache.appcache')
def cache(name=None):
	return render_template('cache.appcache')