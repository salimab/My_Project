from flask import Flask , render_template

app = Flask(__name__)

@app.route("/<string:page_name>/")

def home(page_name):
    return render_template('%s.html' % page_name )

app.run()