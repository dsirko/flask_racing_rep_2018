from flask import Flask, render_template
from main_rep import process_logs
from utils import format_timedelta
from constants import BEST_RACERS

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/report')
def report():
    report = process_logs()
    return render_template('report.html' , report=report, format_timedelta=format_timedelta, BEST_RACERS=BEST_RACERS)


if __name__ == '__main__':
    app.run(debug=True)