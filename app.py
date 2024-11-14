from flask import Flask, render_template
from main_rep import process_logs

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/report')
def report():
    report = process_logs()
    return render_template('report.html' , report=report)


if __name__ == '__main__':
    app.run(debug=True)