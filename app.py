from flask import Flask, render_template, request, jsonify
from app import app as application
from apscheduler.schedulers.background import BackgroundScheduler
from plyer import notification
import datetime

app = Flask(__name__)

# Initialize the scheduler
scheduler = BackgroundScheduler()

@app.route('/')
def index():
    return render_template('index.html')

def notify():
    notification_title = "Time to drink water"
    notification_message = "This is your notification message."

    notification.notify(
        title=notification_title,
        message=notification_message,
        app_name="Notification App"
    )
    log()

def log():
    now = datetime.datetime.now()
    with open("newfile.txt", 'a') as f:
        f.write(f"you drank water {now}\n")

@app.route('/start_notifications', methods=['POST'])
def start_notifications():
    hours = int(request.form['hour'])
    minutes = int(request.form['minute'])
    seconds = int(request.form['second'])
    time_interval = seconds + (minutes * 60) + (hours * 3600)

    scheduler.add_job(notify, 'interval', seconds=time_interval)
    scheduler.start()

    return jsonify({'status': 'Notifications started'})

if __name__ == '__main__':
    app.run()
