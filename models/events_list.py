from models.event import *

event1 = Event("2020/10/31", "Halloween", 30, "Mitchell", "Big party!!")
event2 = Event("2020/12/17", "Christmas", 60, "Sinclair", "Last day!!!")

events = [event1, event2]

def add_new_event(event):
    events.append(event)