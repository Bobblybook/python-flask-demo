from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root_path():
    # Connect to sqlite db
    # grab data from db
    # generate plotly graph
    # export plotly graph to javascript
    posts_python = 'some code eg. json graph'
    return render_template('index.html', posts_html=posts_python)


@app.route('/custom_page')
def page1():
    return 'Page 1'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, True)
