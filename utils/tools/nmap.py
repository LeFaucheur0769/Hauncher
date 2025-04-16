from textual.widget import Widget
from textual.widgets import Button, Header, Footer
from textual.containers import Vertical

class NmapWidget(Widget):
    def compose(self):
        yield Vertical(
            Button("Start Scan", id="scan"),
            Button("Settings", id="settings"),
            Button("Back", id="back")
        )

    def on_button_pressed(self, event):
        if event.button.id == "back":
            self.remove() # Remove the current widgetls
        else:
            self.app.title = f"You pressed: {event.button.label}"
        
    def handle_back(self, event):
        None
