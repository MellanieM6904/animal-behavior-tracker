import models
import datetime
from nicegui import events, ui
import io, csv

def on_behavior(activity, name, temp, bid, treatment, exposure):
    if name.value == '':
        ui.notify(f"Please enter name, green house temp, and butterfly id to record")
        return
    if temp.value == '':
        ui.notify(f"Please enter name, green house temp, and butterfly id to record")
        return
    if bid.value == '':
        ui.notify(f"Please enter name, green house temp, and butterfly id to record")
        return

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
        "Sand": 9,
        "Start": 10,
        "End of Experiment": 11
    }

    if exposure.value == "TRUE": exp = "Experimental Exposure"
    else: exp = "Behavioral Observation"

    behav = behavs[activity]
    models.Activities.create(
        bid = int(bid.value),
        time = datetime.datetime.today(),
        activity = behav,
        temp = temp.value,
        user = name.value,
        treatment = treatment.value,
        exposure = exp
    )

    ui.notify(f"{activity} @ {datetime.datetime.today()} recorded")

def handle_key(e: events.KeyEventArguments, name, temp, bid, treatment, exposure):
    if name.value == '':
        ui.notify(f"Please enter name, green house temp, and butterfly id to record")
        return
    if temp.value == '':
        ui.notify(f"Please enter name, green house temp, and butterfly id to record")
        return
    if bid.value == '':
        ui.notify(f"Please enter name, green house temp, and butterfly id to record")
        return

    if e.action.keyup: return # Prevent duplicate recording
    behav = int(e.key.name)
    if behav not in range(0, 10): 
        ui.notify(f"{behav}: Invalid behavior, select another behavior")
        return

    if exposure.value == "TRUE": exp = "Experimental Exposure"
    else: exp = "Behavioral Observation"
    
    models.Activities.create(
        bid = int(bid.value),
        time = datetime.datetime.today(),
        activity = behav,
        temp = float(temp.value),
        user = name.value,
        treatment = treatment.value,
        exposure = exp
    )

    ui.notify(f"{behav} @ {datetime.datetime.today()} recorded")

def submit_weight(name, bid, treatment, wb, wa):
    if name.value == '':
        ui.notify(f"Please enter name, weight, treatment, and butterfly id to record")
        return
    if treatment.value == '':
        ui.notify(f"Please enter name, weight, treatment, and butterfly id to record")
        return
    if bid.value == '':
        ui.notify(f"Please enter name, weight, treatment, and butterfly id to record")
        return

    models.Weights.create(
        bid = int(bid.value),
        user = name.value,
        time = datetime.datetime.today(),
        treatment = treatment.value,
        weight_before = wb.value,
        weight_after = wa.value
    )

    ui.notify(f"Weights {wa.value, wb.value} for butterfly {bid.value} recorded")

def download_obs():
    query = models.Activities.select()
    colNames = [field.name for field in models.Activities._meta.sorted_fields]
    results = list(query.tuples())
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(colNames)
    writer.writerows(results)

    ui.download.content(output.getvalue(), 'obs_data.csv')

def download_weights():
    query = models.Weights.select()
    colNames = [field.name for field in models.Weights._meta.sorted_fields]
    results = list(query.tuples())
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(colNames)
    writer.writerows(results)

    ui.download.content(output.getvalue(), 'weights_data.csv')