import tkinter as tk
import pyperclip
import requests
from bs4 import BeautifulSoup
from checker import LinkCheckerApp

class SourceCodeModifierApp(LinkCheckerApp):
    def __init__(self, root):
        super().__init__(root)

        # Create a label to display the modified link
        self.modified_link_label = tk.Label(root, text="Modified Link:")
        self.modified_link_label.pack()

    def modify_source_code(self, link):
        # Opens the source code of the website
        source_code = self.get_website_source(link) 
        # modifies the source code as needed
        modified_source_code = self.modify_code(source_code)
        # Prints the modified source code
        print(modified_source_code)
        # Copy the modified source code to the clipboard
        pyperclip.copy(modified_source_code)
        print("Modified")
        # Display the modified link in the label
        self.modified_link_label.config(text=f"Modified Link: {modified_source_code}")


    def get_website_source(self, link):
        try:
            response = requests.get(link)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving website source code: {e}")
            return None

    def modify_code(self, source_code):
        soup = BeautifulSoup(source_code, "html.parser")

        #Finds teh image tage with teh specified class
        image_tag = soup.find("img", class_="background-gif")

        if image_tag:
            # Get the src attribute from the image tag
            image_src = image_tag["src"]

            modified_src = image_src

            # Perform replacements in a specific order to avoid unintended changes
            modified_src = modified_src.replace("ask_previews", "ask_video")  # Replace "ask_previews" first
            modified_src = modified_src.replace("previews", "encoded")  # Then replace "previews"
            modified_src = modified_src.replace("_large.jpg", ".mp4")
            modified_src = modified_src.replace(".gif", ".mp4")

            return modified_src
        else:
            print("Image tag with class 'background-gif' not found")
            return None

def main():
    root = tk.Tk()
    app = SourceCodeModifierApp(root)
    # Bind a button or event to trigger the modification process
    app.check_button.config(command=lambda: app.modify_source_code(app.link_entry.get()))  # Bind to check button
    root.mainloop()

if __name__ == "__main__":
    main()
