import models
import events

from nicegui import app, ui

with ui.tabs().classes('w-full') as tabs:
    one = ui.tab('Record')
    two = ui.tab('Results')

with ui.tab_panels(tabs, value=one).classes('w-full'):
    with ui.tab_panel(one):
        with ui.card().classes("max-w-3xl mx-auto shadow-lg"):
            with ui.row().classes("w-full justify-center"):
                name = ui.input("Your Name")
                temp = ui.input("Greenhouse Temperature")
                bid = ui.input("Butterfly ID")
                with ui.grid(columns = 2):
                    ui.button("Land/Perch", color = "#A7C7A3").on("click", lambda: events.on_behavior("Land", name, temp, bid))
                    ui.label("[0]").style("font-size: 150%; font-weight: 300")
                    ui.button("Bask", color = "#A7C7A3").on("click", lambda: events.on_behavior("Bask", name, temp, bid))
                    ui.label("[1]").style("font-size: 150%; font-weight: 300")
                    ui.button("Fly", color = "#A7C7A3").on("click", lambda: events.on_behavior("Fly", name, temp, bid))
                    ui.label("[2]").style("font-size: 150%; font-weight: 300")
                    ui.button("Feed", color = "#A7C7A3").on("click", lambda: events.on_behavior("Feed", name, temp, bid))
                    ui.label("[3]").style("font-size: 150%; font-weight: 300")
                    ui.button("Flutter", color = "#A7C7A3").on("click", lambda: events.on_behavior("Flutter", name, temp, bid))
                    ui.label("[4]").style("font-size: 150%; font-weight: 300")
                    ui.button("Walk", color = "#A7C7A3").on("click", lambda: events.on_behavior("Walk", name, temp, bid))
                    ui.label("[5]").style("font-size: 150%; font-weight: 300")

        ui.keyboard(on_key = lambda e: events.handle_key(e, name, temp, bid))

    with ui.tab_panel(two):
        with ui.card().classes("max-w-3xl mx-auto shadow-lg"):
            with ui.row().classes("w-full justify-center"):
                ui.button("Download Results (.csv)", color = "#A7C7A3").on("click", lambda: events.download_res())


ui.run()