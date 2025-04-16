"""
An App to show the current time.
"""
"""
Imports
"""
import importlib

"""
Textual imports
"""
from textual import on
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Button, Header, Footer, Select
from textual.containers import Vertical
from textual.binding import Binding

"""
"""

"""
utils imports
"""
from utils.tools.files import get_files
from utils.tui.clear_term import clear_terminal
from utils.tools.nmap import NmapWidget

LINES = get_files().splitlines()

        
            
class Hauncher(App):                                  
    BINDINGS = [
        Binding(key="x", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding(key="delete", action="delete", description="Delete the thing"),
        Binding(key="j", action="down", description="Scroll down", show=False),
    ]
    CSS = """
    Screen { align: center middle; }
    Digits { width: auto; }
    """

    def compose(self) -> ComposeResult:
        """
        Compose the UI layout by yielding the Digits widget.

        This method constructs the UI components that will be used in the
        application. It yields a Digits widget initialized with an empty string,
        which will be used to display the current time.

        Returns:
            ComposeResult: A generator yielding the UI components.
        """
        yield Header()
        yield Footer()
        yield Select.from_values(LINES)

    @on(Select.Changed)

    def select_changed(self, event : Select.Changed) -> None:
        if str(event.value).lower() == "nmap":
            self.mount(NmapWidget())
            

        


    def footer(self) -> None:
        """
        Updates the displayed time with the current time.

        This method is called every second, and it retrieves the current time
        using datetime.now().time() and formats it as a string with
        f"{clock:%T}". The formatted string is then passed to the update
        method of the Digits widget to display the current time.

        Returns:
            None
        """



if __name__ == "__main__":
    try:
        app = Hauncher()
        app.run()
    finally:
        # clear_terminal()
        # break  # Remove this `break` if you want to return after sub-app exits
        pass