import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import requests
from io import BytesIO

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
        return bibtex_entry
    except requests.exceptions.RequestException as e:
        return f"Error fetching {doi}: {e}"

def fetch_bibtex():
    input_text = doi_textbox.get("1.0", tk.END).strip()
    possible_separators = [',', '\n']
    for sep in possible_separators:
        input_text = input_text.replace(sep, ' ')
    doi_list = input_text.split()
    include_abstract = abstract_var.get()
    output_text.delete("1.0", tk.END)
    combined_bibtex = []
    for doi in doi_list:
        bibtex = get_bibtex(doi, include_abstract=include_abstract)
        combined_bibtex.append(bibtex)
    output_text.insert(tk.END, "\n\n".join(combined_bibtex))

def copy_bibtex():
    bibtex_text = output_text.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(bibtex_text)

def restart():
    doi_textbox.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    abstract_var.set(False)

def open_link(url):
    import webbrowser
    webbrowser.open_new(url)

def exit_application():
    root.destroy()

root = tk.Tk()
root.title("DOI2BibTeX Fetcher")
root.configure(bg="#f5f5f5")

# Top frame for logo and links
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

# Scholar and GitHub links (right)
link_frame = tk.Frame(top_frame, bg="#0073e6")
link_frame.pack(side=tk.RIGHT, padx=10)

# Google Scholar logo and link
scholar_logo_url = "https://raw.githubusercontent.com/AhsanKhodami/doi2bibtex/refs/heads/main/google-scholar.256x256.png"
response = requests.get(scholar_logo_url)
scholar_logo_image = Image.open(BytesIO(response.content))
scholar_logo_image.thumbnail((25, 25))
scholar_logo = ImageTk.PhotoImage(scholar_logo_image)

scholar_button = tk.Button(link_frame, image=scholar_logo, command=lambda: open_link("https://scholar.google.com/citations?user=WCqPnS4AAAAJ&hl=en"), bg="#0073e6", borderwidth=0)
scholar_button.pack(side=tk.TOP, pady=2)

scholar_text = tk.Label(link_frame, text="Google Scholar", bg="#0073e6", fg="white", font=("Helvetica", 10, "bold"), cursor="hand2")
scholar_text.pack(side=tk.TOP)
scholar_text.bind("<Button-1>", lambda e: open_link("https://scholar.google.com/citations?user=WCqPnS4AAAAJ&hl=en"))

# GitHub logo and link
github_logo_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
response = requests.get(github_logo_url)
github_logo_image = Image.open(BytesIO(response.content))
github_logo_image.thumbnail((25, 25))
github_logo = ImageTk.PhotoImage(github_logo_image)

github_button = tk.Button(link_frame, image=github_logo, command=lambda: open_link("https://github.com/AhsanKhodami/doi2bibtex"), bg="#0073e6", borderwidth=0)
github_button.pack(side=tk.TOP, pady=2)

github_text = tk.Label(link_frame, text="GitHub", bg="#0073e6", fg="white", font=("Helvetica", 10, "bold"), cursor="hand2")
github_text.pack(side=tk.TOP)
github_text.bind("<Button-1>", lambda e: open_link("https://github.com/AhsanKhodami/doi2bibtex"))

# Instruction label
prompt_label = tk.Label(
    root, text="Enter one or more DOIs (separated by space, comma, or new lines):",
    bg="#f5f5f5", font=("Helvetica", 12, "bold")
)
prompt_label.pack(pady=5)

# Text box for entering DOIs
doi_textbox = tk.Text(root, width=70, height=5, font=("Helvetica", 10))
doi_textbox.pack(padx=5, pady=5)

# Checkbox for abstract
abstract_var = tk.BooleanVar(value=False)
abstract_check = tk.Checkbutton(root, text="Include abstract", variable=abstract_var, bg="#f5f5f5", font=("Helvetica", 10))
abstract_check.pack(pady=5)

# Fetch button
fetch_button = tk.Button(root, text="Fetch BibTeX", command=fetch_bibtex, bg="#4caf50", fg="white", font=("Helvetica", 10, "bold"))
fetch_button.pack(pady=5)

# Label for output
output_label = tk.Label(root, text="BibTeX Output:", bg="#f5f5f5", font=("Helvetica", 12, "bold"))
output_label.pack(pady=5)

# Text box for BibTeX output
output_text = tk.Text(root, width=80, height=15, font=("Helvetica", 10))
output_text.pack(padx=5, pady=5)

# Copy, Restart, and Exit buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_bibtex, bg="#2196f3", fg="white", font=("Helvetica", 10, "bold"))
copy_button.pack(side=tk.LEFT, padx=10)

restart_button = tk.Button(button_frame, text="Restart", command=restart, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"))
restart_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Exit Application", command=exit_application, bg="#9e9e9e", fg="white", font=("Helvetica", 10, "bold"))
exit_button.pack(side=tk.LEFT, padx=10)

# Footer text
footer_label = tk.Label(root, text="© 2025 Khodami.site", bg="#f5f5f5", font=("Helvetica", 10))
footer_label.pack(pady=5)

root.mainloop()