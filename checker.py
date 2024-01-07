import tkinter as tk
import pyperclip
import requests
import re
class LinkCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Useless Numerading")

        # Create entry widget to display and input the link
        self.link_entry = tk.Entry(root, width=60)
        self.link_entry.pack(pady=10)

        # Create a button to check the link
        self.check_button = tk.Button(root, text="Check Link", command=self.check_link)
        self.check_button.pack(pady=10)

        # Bind the Enter key to the check_link function
        self.root.bind('<Return>', lambda event=None: self.check_link())

    def check_link(self):
        # Get the link from the entry widget
        link = self.link_entry.get()

        # Perform your link validation logic here
        if self.is_valid_link(link):
            print(f"Link is valid: {link}")
        else:
            print(f"Invalid link: {link}")
            self.root.destroy()

    def is_valid_link(self, link):
        # Check if the link is related to https://www.numerade.com/ask/question/
        url_pattern = re.compile(r'https://www.numerade.com/ask/question/')
        return bool(url_pattern.match(link))

def main():
    root = tk.Tk()
    app = LinkCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
