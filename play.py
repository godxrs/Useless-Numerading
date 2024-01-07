import tkinter as tk
import webbrowser
import pyperclip
from source_checker_modifier import SourceCodeModifierApp  # Import the class from "source.py"

class PlayerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.source_checker = SourceCodeModifierApp(self)  # Create instance for link modification

        # Modified link display
        self.modified_link_label = tk.Label(self, text="Modified Link:")
        self.modified_link_label.pack()
        self.modified_link_text = tk.Entry(self, width=40)  # Editable for copying
        self.modified_link_text.pack()


        # Add a button to paste the link from the clipboard
        self.paste_link_button = tk.Button(self, text="Paste Link", command=self.paste_link)
        self.paste_link_button.pack()

        # Show Video button
        self.show_video_button = tk.Button(self, text="Show Video", command=self.play_video)
        self.show_video_button.pack()

        self.source_checker.check_button.config(command=self.modify_and_display_link)

    def modify_and_display_link(self):
        modified_link = self.source_checker.modify_source_code(self.source_checker.link_entry.get())
        self.modified_link_text.delete(0, tk.END)  # Clear previous content
        self.modified_link_text.insert(0, modified_link)  # Display the modified link
    
    def paste_link(self):
        pasted_link = pyperclip.paste()  # Paste from clipboard
        self.modified_link_text.delete(0, tk.END)  # Clear previous content
        self.modified_link_text.insert(0, pasted_link)  # Insert the pasted link

    def play_video(self):
        modified_link = self.modified_link_text.get()
        if modified_link:
            webbrowser.open(modified_link)  # Open the modified link in a browser for playback
        else:
            print("Error: No modified link available to play.")

if __name__ == "__main__":
    app = PlayerApp()
    app.mainloop()
