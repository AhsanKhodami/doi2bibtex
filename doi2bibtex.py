import tkinter as tk
from tkinter import PhotoImage, filedialog, ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os
import time
import webbrowser

# Global variable to store the path of the file where data is saved
saved_file_path = None
unsaved_changes = False  # Tracks whether there are unsaved changes

def open_link(url):
    webbrowser.open_new(url)

def send_email(email_address):
    webbrowser.open(f"mailto:{email_address}")

def get_bibtex(doi, include_abstract=False):
    doi = doi.strip()
    doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "").replace("doi.org/", "")
    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        bibtex_entry = response.text
        if not include_abstract:
            cleaned_lines = [line for line in bibtex_entry.split('\n') if not line.strip().lower().startswith('abstract')]
            bibtex_entry = '\n'.join(cleaned_lines).strip()
        # Filter out non-alphabetic characters (excluding common BibTeX symbols)
        bibtex_entry = ''.join(char for char in bibtex_entry if char.isprintable())
        return bibtex_entry
    except requests.exceptions.RequestException as e:
        return f"Error fetching {doi}: {e}"

def fetch_bibtex():
    global unsaved_changes
    input_text = doi_textbox.get("1.0", tk.END).strip()
    possible_separators = [',', '\n']
    for sep in possible_separators:
        input_text = input_text.replace(sep, ' ')
    doi_list = input_text.split()
    include_abstract = abstract_var.get()
    output_text.delete("1.0", tk.END)
    combined_bibtex = []
    progress_bar['maximum'] = len(doi_list)
    for i, doi in enumerate(doi_list, start=1):
        bibtex = get_bibtex(doi, include_abstract=include_abstract)
        combined_bibtex.append(bibtex)
        progress_bar['value'] = i
        root.update_idletasks()  # Update the progress bar
    output_text.insert(tk.END, "\n\n".join(combined_bibtex))

    # If auto-save is enabled, save automatically without asking for file location
    if auto_save_var.get():
        save_bibtex_to_file(combined_bibtex)
    else:
        unsaved_changes = True  # Mark unsaved changes

    progress_bar['value'] = 0  # Reset the progress bar

def copy_bibtex():
    bibtex_text = output_text.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(bibtex_text)

def restart():
    global unsaved_changes
    if unsaved_changes:
        confirm = messagebox.askyesnocancel("Unsaved Changes", "You have unsaved changes. Do you want to save them before restarting?")
        if confirm is None:  # Cancel
            return
        elif confirm:  # Yes, save changes
            save_to_file()
    # Reset the application
    doi_textbox.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    abstract_var.set(False)
    auto_save_var.set(False)
    progress_bar['value'] = 0
    unsaved_changes = False

def exit_application():
    global unsaved_changes
    if unsaved_changes:
        confirm = messagebox.askyesnocancel("Unsaved Changes", "You have unsaved changes. Do you want to save them before exiting?")
        if confirm is None:  # Cancel
            return
        elif confirm:  # Yes, save changes
            save_to_file()
    root.destroy()

def save_bibtex_to_file(bibtex_entries):
    global saved_file_path, unsaved_changes  # Access global variables

    # If no file path is saved yet, prompt the user for the file location
    if saved_file_path is None:
        saved_file_path = filedialog.asksaveasfilename(defaultextension=".bib", filetypes=[("BibTeX files", "*.bib"), ("Text files", "*.txt")])
    
    # If the user cancels the save, return
    if not saved_file_path:
        message_label.config(text="Save operation canceled", fg="red")
        return

    # Open the file in append mode and write the new BibTeX entries
    with open(saved_file_path, "a", encoding="utf-8") as f:
        f.write("\n".join(bibtex_entries))
    
    # Show the location and timestamp of the saved file
    timestamp = time.strftime("%H:%M:%S")
    message_label.config(text=f"Data saved to {saved_file_path} at {timestamp}", fg="green")
    unsaved_changes = False  # Mark changes as saved

def save_to_file():
    global unsaved_changes
    bibtex_text = output_text.get("1.0", tk.END).strip()
    if not bibtex_text:
        message_label.config(text="No BibTeX to save!", fg="red")
        return
    save_bibtex_to_file([bibtex_text])
    unsaved_changes = False  # Mark changes as saved

root = tk.Tk()
root.title("DOI2BibTeX Fetcher")
root.configure(bg="#f5f5f5")

# Top frame for logo, links, and buttons
top_frame = tk.Frame(root, bg="#0073e6", height=100)
top_frame.pack(fill=tk.X)

# Main logo (left)
logo_url = "https://raw.githubusercontent.com/AhsanKhodami/doi2bibtex/refs/heads/main/khodami%20site%20logo%20light%20536x.png"
response = requests.get(logo_url)
logo_image = Image.open(BytesIO(response.content))
logo_image.thumbnail((75, 75))
logo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(top_frame, image=logo, bg="#0073e6")
logo_label.pack(side=tk.LEFT, padx=10, pady=10)

# Header text
header_label = tk.Label(
    top_frame, text="DOI2BibTeX Fetcher", font=("Helvetica", 16, "bold"), fg="white", bg="#0073e6"
)
header_label.pack(side=tk.LEFT, padx=20)

# Button links frame
button_links_frame = tk.Frame(top_frame, bg="#0073e6")
button_links_frame.pack(side=tk.RIGHT, padx=10)

# Visit My Website button
visit_icon_url = "https://cdn-icons-png.flaticon.com/512/1040/1040243.png"
response = requests.get(visit_icon_url)
visit_icon_image = Image.open(BytesIO(response.content))
visit_icon_image.thumbnail((25, 25))
visit_icon = ImageTk.PhotoImage(visit_icon_image)

visit_button = tk.Button(button_links_frame, image=visit_icon, text="Visit My Website", compound=tk.LEFT, command=lambda: open_link("https://khodami.site"), bg="#0073e6", fg="white", font=("Helvetica", 10, "bold"), borderwidth=0)
visit_button.pack(side=tk.LEFT, padx=5)

# Help button
help_icon_url = "https://cdn-icons-png.flaticon.com/512/189/189664.png"
response = requests.get(help_icon_url)
help_icon_image = Image.open(BytesIO(response.content))
help_icon_image.thumbnail((25, 25))
help_icon = ImageTk.PhotoImage(help_icon_image)

help_button = tk.Button(button_links_frame, image=help_icon, text="Help", compound=tk.LEFT, command=lambda: open_link("https://ahsankhodami.github.io/doi2bibtex/#how-to-use"), bg="#0073e6", fg="white", font=("Helvetica", 10, "bold"), borderwidth=0)
help_button.pack(side=tk.LEFT, padx=5)

# Contact button
contact_icon_url = "https://cdn-icons-png.flaticon.com/512/732/732200.png"
response = requests.get(contact_icon_url)
contact_icon_image = Image.open(BytesIO(response.content))
contact_icon_image.thumbnail((25, 25))
contact_icon = ImageTk.PhotoImage(contact_icon_image)

contact_button = tk.Button(button_links_frame, image=contact_icon, text="Contact", compound=tk.LEFT, command=lambda: send_email("ahsan.khodami@gmail.com"), bg="#0073e6", fg="white", font=("Helvetica", 10, "bold"), borderwidth=0)
contact_button.pack(side=tk.LEFT, padx=5)

# Instruction label
prompt_label = tk.Label(
    root, text="Enter one or more DOIs (separated by space, comma, or new lines):",
    bg="#f5f5f5", font=("Helvetica", 12, "bold")
)
prompt_label.pack(pady=5)

# Text box for entering DOIs
doi_textbox = tk.Text(root, width=70, height=5, font=("Helvetica", 10))
doi_textbox.pack(padx=5, pady=5)

# Frame for checkboxes (horizontally aligned)
checkbox_frame = tk.Frame(root, bg="#f5f5f5")
checkbox_frame.pack(pady=5)

# Checkbox for abstract
abstract_var = tk.BooleanVar(value=False)
abstract_check = tk.Checkbutton(checkbox_frame, text="Include abstract", variable=abstract_var, bg="#f5f5f5", font=("Helvetica", 10))
abstract_check.pack(side=tk.LEFT, padx=10)

# Checkbox for auto-save
auto_save_var = tk.BooleanVar(value=False)
auto_save_check = tk.Checkbutton(checkbox_frame, text="Auto-save after fetch", variable=auto_save_var, bg="#f5f5f5", font=("Helvetica", 10))
auto_save_check.pack(side=tk.LEFT, padx=10)

# Progress bar
progress_bar = ttk.Progressbar(root, length=400, mode='determinate')
progress_bar.pack(pady=5)

# Frame for Fetch and Save buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

fetch_button = tk.Button(button_frame, text="Fetch BibTeX", command=fetch_bibtex, bg="#4caf50", fg="white", font=("Helvetica", 10, "bold"))
fetch_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(button_frame, text="Save to file", command=save_to_file, bg="#4caf50", fg="white", font=("Helvetica", 10, "bold"))
save_button.pack(side=tk.LEFT, padx=10)

# Label for saved message
message_label = tk.Label(root, text="", bg="#f5f5f5", font=("Helvetica", 10, "bold"))
message_label.pack(pady=5)

# Label for output
output_label = tk.Label(root, text="BibTeX Output:", bg="#f5f5f5", font=("Helvetica", 12, "bold"))
output_label.pack(pady=5)

# Text box with scrollbars for BibTeX output
output_frame = tk.Frame(root)
output_frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

output_scrollbar = tk.Scrollbar(output_frame, orient=tk.VERTICAL)
output_text = tk.Text(output_frame, wrap=tk.NONE, yscrollcommand=output_scrollbar.set, font=("Helvetica", 10))
output_scrollbar.config(command=output_text.yview)
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Copy, Restart, and Exit buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_bibtex, bg="#2196f3", fg="white", font=("Helvetica", 10, "bold"))
copy_button.pack(side=tk.LEFT, padx=10)

restart_button = tk.Button(button_frame, text="Restart", command=restart, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"))
restart_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Exit Application", command=exit_application, bg="#9e9e9e", fg="white", font=("Helvetica", 10, "bold"))
exit_button.pack(side=tk.LEFT, padx=10)

footer_label = tk.Label(root, text="© 2025 Khodami.site", bg="#f5f5f5", font=("Helvetica", 10))
footer_label.pack(pady=5)

root.mainloop()
