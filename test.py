import models
import events

from nicegui import app, ui

with ui.tabs().classes('w-full') as tabs:
    one = ui.tab('Observations')
    two = ui.tab('Weights')
    three = ui.tab('Results')

with ui.tab_panels(tabs, value=one).classes('w-full'):
    with ui.tab_panel(one):
        with ui.card().classes("max-w-3xl mx-auto shadow-lg"):
            with ui.row().classes("w-full justify-center"):
                name = ui.input("Your Name")
                temp = ui.input("Greenhouse Temperature")
                bid = ui.input("Butterfly ID")
                treatment = ui.input("Control/Low/High") # Make dropdown selection
                exposure = ui.checkbox("Experimental exposure?")
                # Add M/F checkbox after Control observations
                with ui.grid(columns = 2):
                    ui.button("Land/Perch", color = "#A7C7A3").on("click", lambda: events.on_behavior("Land", name, temp, bid, treatment, exposure))
                    ui.label("[0]").style("font-size: 150%; font-weight: 300")
                    ui.button("Bask", color = "#A7C7A3").on("click", lambda: events.on_behavior("Bask", name, temp, bid, treatment, exposure))
                    ui.label("[1]").style("font-size: 150%; font-weight: 300")
                    ui.button("Fly", color = "#A7C7A3").on("click", lambda: events.on_behavior("Fly", name, temp, bid, treatment, exposure))
                    ui.label("[2]").style("font-size: 150%; font-weight: 300")
                    ui.button("Feed", color = "#A7C7A3").on("click", lambda: events.on_behavior("Feed", name, temp, bid, treatment, exposure))
                    ui.label("[3]").style("font-size: 150%; font-weight: 300")
                    ui.button("Flutter", color = "#A7C7A3").on("click", lambda: events.on_behavior("Flutter", name, temp, bid, treatment, exposure))
                    ui.label("[4]").style("font-size: 150%; font-weight: 300")
                    ui.button("Walk", color = "#A7C7A3").on("click", lambda: events.on_behavior("Walk", name, temp, bid, treatment, exposure))
                    ui.label("[5]").style("font-size: 150%; font-weight: 300")
                    ui.button("Puddling", color = "#A7C7A3").on("click", lambda: events.on_behavior("Puddling", name, temp, bid, treatment, exposure))
                    ui.label("[6]").style("font-size: 150%; font-weight: 300")
                    ui.button("Oviposit/Mating", color = "#A7C7A3").on("click", lambda: events.on_behavior("Reproductive", name, temp, bid, treatment, exposure))
                    ui.label("[7]").style("font-size: 150%; font-weight: 300")
                    ui.button("[F] Land on thistle]", color = "#A7C7A3").on("click", lambda: events.on_behavior("Thistle", name, temp, bid, treatment, exposure))
                    ui.label("[8]").style("font-size: 150%; font-weight: 300")
                    ui.button("[M] Socializing]", color = "#A7C7A3").on("click", lambda: events.on_behavior("Socializing", name, temp, bid, treatment, exposure))
                    ui.label("[9]").style("font-size: 150%; font-weight: 300")
                    ui.button("Start Experiment", color = "#A7C7A3").on("click", lambda: events.on_behavior("Start", name, temp, bid, treatment, exposure))
                    ui.button("End of Experiment", color = "#A7C7A3").on("click", lambda: events.on_behavior("End of Experiment", name, temp, bid, treatment, exposure))

        ui.keyboard(on_key = lambda e: events.handle_key(e, name, temp, bid, treatment, exposure))

    with ui.tab_panel(two):
        with ui.card().classes("max-w-3xl mx-auto shadow-lg"):
            with ui.column().classes("w-full justify-center"):
                with ui.row().classes("w-full justify-center"):
                    n = ui.input("Your Name")
                    b = ui.input("Butterfly ID")
                    t = ui.input("Control/Low/High")
                    w = ui.input("Weight (g)")
                ui.button("Submit", color = "#A7C7A3").on("click", lambda: events.submit_weight(n, b, t, w))

    with ui.tab_panel(three):
        with ui.card().classes("max-w-3xl mx-auto shadow-lg"):
            with ui.column().classes("w-full justify-center"):
                ui.button("Download Observation Results (.csv)", color = "#A7C7A3").on("click", lambda: events.download_obs())
                ui.button("Download Weight Results (.csv)", color = "#A7C7A3").on("click", lambda: events.download_weights())


ui.run()