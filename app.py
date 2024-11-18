from flask import Flask, render_template, url_for, request
from main_rep import process_logs
from utils import format_timedelta, find_driver_info
from constants import BEST_RACERS

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# def get_driver_info(driver_id):
#     result = find_driver_info(driver_id)
#     return render_template('driver_info.html', driver = result)


@app.route('/report')
def report():
    report = process_logs()
    return render_template('report.html' , report=report, format_timedelta=format_timedelta, BEST_RACERS=BEST_RACERS)


@app.route('/report/drivers/')
def report_drivers():
    driver_id = request.args.get('driver_id')
    if driver_id:
        report = process_logs()
        driver = find_driver_info(report, driver_id)
        return render_template('driver_info.html', driver=driver)
    else:
        report = process_logs()
        print("report_drivers")
        return render_template('report_drivers.html' , report=report)



if __name__ == '__main__':
    app.run(debug=True)