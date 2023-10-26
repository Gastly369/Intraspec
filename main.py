import tkinter as tk
from tkinter import messagebox
from test import BigFiveTest
class BigFiveApp(tk.Tk):
   def __init__(self):
        super().__init__()
        self.title("Big Five Personality Test")
      self.geometry("800x600")
        self.resizable(False, False)
        self.test = BigFiveTest()        self.create_widgets()
    def create_widgets(self):
        # Create UI elements
        self.label = tk.Label(self, text="Welcome to the Big Five Personality Test!")
        self.label.pack(pady=20)
        self.start_button = tk.Button(self, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)
    def start_test(self):
        # Start the test
        result = messagebox.askyesno("Confirmation", "Are you ready to start the test?")
        if result:
            self.destroy()
           self.test.start()
if __name__ == "__main__":
   app = BigFiveApp()
   app.mainloop()
