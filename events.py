import models
import datetime
from nicegui import events, ui
import io, csv

def on_behavior(activity, name, temp, id, treatment, exposure):
    if name.value == '': ui.notify(f"Please enter name, green house temp, and butterfly id to record")
    if temp.value == '': ui.notify(f"Please enter name, green house temp, and butterfly id to record")
    if id.value == '': ui.notify(f"Please enter name, green house temp, and butterfly id to record")

    behavs = {
        "Land": 0,
        "Bask": 1,
        "Fly": 2,
        "Feed": 3,
        "Flutter": 4,
        "Walk": 5,
        "Puddling": 6,
        "Reproductive": 7,
        "Thistle": 8,
        "Socializing": 9,
        "Start": 10,
        "End of Experiment": 11
    }

    behav = behavs[activity]
    models.Activities.create(
        bid = int(id.value),
        time = datetime.datetime.today(),
        activity = behav,
        temp = temp.value,
        user = name.value,
        treatment = treatment.value,
        exposure = exposure.value
    )

    ui.notify(f"{activity} @ {datetime.datetime.today()} recorded")

def handle_key(e: events.KeyEventArguments, name, temp, id, treatment, exposure):
    if name.value == '': ui.notify(f"Please enter name, green house temp, and butterfly id to record")
    if temp.value == '': ui.notify(f"Please enter name, green house temp, and butterfly id to record")
    if id.value == '': ui.notify(f"Please enter name, green house temp, and butterfly id to record")

    if e.action.keyup: return # Prevent duplicate recording
    behav = int(e.key.name)
    if behav not in range(0, 10): 
        ui.notify(f"{behav}: Invalid behavior, select another behavior")
        return
    
    models.Activities.create(
        bid = int(id.value),
        time = datetime.datetime.today(),
        activity = behav,
        temp = float(temp.value),
        user = name.value,
        treatment = treatment.value,
        exposure = exposure.value
    )

    ui.notify(f"{behav} @ {datetime.datetime.today()} recorded")

def download_res():
    query = models.Activities.select()
    colNames = [field.name for field in models.Activities._meta.sorted_fields]
    results = list(query.tuples())
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(colNames)
    writer.writerows(results)

    ui.download.content(output.getvalue(), 'data.csv')