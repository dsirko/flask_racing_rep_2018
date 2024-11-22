from flask import Flask, render_template, url_for, request
from main_rep import process_logs
from utils import format_timedelta, find_driver_info
from constants import BEST_RACERS

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Race report!</h1>'


@app.route('/report/')
def report():
    """ Displays a report of race results. The report can be sorted """
    order = request.args.get('order', default='asc')
    report = process_logs()
    desc_sorted = sorted(report, key=lambda x: x[3], reverse=(order == 'desc'))
    return render_template('report.html' , report=desc_sorted, format_timedelta=format_timedelta, BEST_RACERS=BEST_RACERS)


@app.route('/report/drivers/')
def report_drivers():
    """ Displays a report of race results for each driver. The report can be sorted """
    driver_id = request.args.get('driver_id')
    order = request.args.get('order', default='asc')
    if driver_id:
        report = process_logs()
        driver = find_driver_info(report, driver_id)
        return render_template('driver_info.html', driver=driver)
    else:
        report = process_logs()
        desc_sorted = sorted(report, key=lambda x: x[1], reverse=(order == 'desc'))
        return render_template('report_drivers.html' , report=desc_sorted)


if __name__ == '__main__':
    app.run(debug=True)