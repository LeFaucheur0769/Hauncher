"""
An App to show the current time.
"""

from datetime import datetime

from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, Select

LINES = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.""".splitlines()


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
        self.title = str(event.value)
        """
        Called when the app is ready to start.

        This method is called once the application is ready to start. It
        schedules the update_clock method to be called every second to
        update the displayed time.

        Returns:
            None
        """
        # self.update_clock()
        # self.set_interval(1, self.update_clock)

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
    app = Hauncher()
    app.run()