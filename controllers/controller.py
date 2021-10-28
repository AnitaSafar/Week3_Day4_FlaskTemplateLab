from flask import render_template, request
from app import app
from models.events_list import add_new_event, events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    print(request.form)
    event_name = request.form["event_name"]
    event_date = request.form["event_date"]
    num_guests = request.form['num_guests']
    room = request.form["room"]
    description = request.form["description"]
    new_event = Event(event_name, event_date, num_guests, room, description)
    add_new_event(new_event)
    return render_template('index.html', title='Events', events=events)