from flask import Flask, render_template
from flask_flatpages import FlatPages
 
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
 
app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/blog/')
def my_blog():
    return render_template('blog.html', pages=pages)
 
@app.route('/resume/')
def show_static_pdf():
    return render_template('resume2.html')

@app.route('/blog/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
 
#
# Below for testing only
#
if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)
