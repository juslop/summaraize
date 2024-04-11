from ttkbootstrap import Label, Frame

class Spinner:
    """
    Show action on-going to user
    """
    def __init__(self, frame: Frame):
        """
        Parameters:
            frame: ttk.Frame
        """
        container = Frame(frame)
        self.label_1 = Label(container, text="")
        self.label_2 = Label(container, text="")
        self.label_1.pack(side="left", pady=5, padx=5)
        self.label_2.pack(side="left", pady=5, padx=5)
        self._spinner = ['|', '/', '-', '\\']
        self._len_spinner = len(self._spinner)
        container.pack()

    def spin(self, counter: int) -> None:
        if self.label_1["text"] == "":
            self.label_1.config(
                text="Processing")
            self.label_2.config(
                text=f"{self._spinner[counter]}"
            )
        else:
            self.label_2.config(
                text=f"{self._spinner[counter % self._len_spinner]}")

    def set_text(self, text: str) -> None:
        self.label_1.config(text=text)

    def stop(self) -> None:
        self.label_1.config(text="")
        self.label_2.config(text="")
