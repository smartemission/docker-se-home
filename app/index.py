import os, sys
import logging
from functools import wraps, update_wrapper
from datetime import datetime
from flask import Flask, render_template, make_response
from reverseproxied import ReverseProxied
from config import config

if __name__ != '__main__':
    # When run with WSGI in Apache we need to extend the PYTHONPATH to find Python modules relative to index.py
    sys.path.insert(0, os.path.dirname(__file__))

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)
app.debug = True

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')

log = logging.getLogger(__name__)
log.setLevel(config['loglevel'])


# Wrapper to disable any kind of caching for all pages
# See http://arusahni.net/blog/2014/03/flask-nocache.html
def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)


# Home page
@app.route('/')
@nocache
def home():
    return page('home')

# Specific page
@app.route('/<string:page_name>')
@nocache
def page(page_name):
    page = '%s%s' % (page_name, '.html')

    # page must be under templates, otherwise try static page
    template_file = os.path.join(os.path.dirname(__file__), 'templates', page)
    if not os.path.isfile(template_file):
        page = '404.html'

    # Let Flask/Jinja2 render the page
    return render_template(page)


if __name__ == '__main__':
    # Run as main via python index.py
    app.run(debug=True, host='0.0.0.0')
