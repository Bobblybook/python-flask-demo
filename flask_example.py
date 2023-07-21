#!venv/bin/python

from flask import Flask, render_template
import plotly.express as px
from json import dumps
from plotly import utils

app = Flask(__name__)


@app.route('/')
def root_path():
    return render_template('index.html')


@app.route('/greenhouse')
def greenhouse():
    # Connect to sqlite db
    # grab data from db
    # generate plotly graph

    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                     size='petal_length', hover_data=['petal_width'])
    fig_json = dumps(fig, cls=utils.PlotlyJSONEncoder)

    return render_template('greenhouse.html', graph_JSON=fig_json)


# Start the web server, only if this script is run directly.
# In a production environment this would not be run this way and the
# Flask code would be hosted using an external WRGI server for stability/performance.
if __name__ == '__main__':
    app.run('0.0.0.0', 8080, True)
