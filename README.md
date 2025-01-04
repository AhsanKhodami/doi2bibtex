# DOI2BibTeX Fetcher

![DOI2BibTeX Fetcher](https://raw.githubusercontent.com/AhsanKhodami/doi2bibtex/refs/heads/main/mainapplication.png)

DOI2BibTeX Fetcher is a simple and intuitive Python-based GUI application designed to fetch BibTeX entries for DOIs (Digital Object Identifiers). It provides additional customization, such as including or excluding abstracts, and offers user-friendly features like copying BibTeX entries to the clipboard.

---

## Features

- Fetch BibTeX entries for one or more DOIs.
- Optionally include or exclude the abstract from BibTeX entries.
- Copy fetched BibTeX entries directly to the clipboard for easy use.
- Restart the application to input new DOIs.
- Provides quick links to the application's **Google Scholar profile** and **GitHub repository** for further resources.
- Clean and modern GUI for seamless user experience.

---

## How to Use

### 1. Launch the Application
Once the application is running, you'll see the interface with the following components:
- **Top Section**:
  - The application's logo.
  - A header titled **"DOI2BibTeX Fetcher"**.
  - Links to the **Google Scholar** profile and **GitHub repository**.
- **DOI Input Field**: A text box where you can enter one or more DOIs (separated by space, comma, or new lines).
- **Abstract Option**: A checkbox to include or exclude abstracts in the BibTeX entries.
- **Control Buttons**: Buttons to fetch BibTeX, copy to clipboard, restart the form, or exit the application.
- **Output Field**: A larger text box to display the fetched BibTeX entries.

### 2. Enter DOIs
Input one or more DOIs into the text box. You can use any of the following formats:
- Space-separated: `10.1234/example1 10.5678/example2`
- Comma-separated: `10.1234/example1, 10.5678/example2`
- Newline-separated:
  ```
  10.1234/example1
  10.5678/example2
  ```

### 3. Fetch BibTeX
- Click the **"Fetch BibTeX"** button.
- The application retrieves BibTeX entries for all valid DOIs entered in the input field.
- BibTeX entries will appear in the output field.

### 4. Include/Exclude Abstract
- Check the **"Include Abstract"** option if you want BibTeX entries to include abstracts.
- Leave it unchecked to exclude abstracts.

### 5. Copy to Clipboard
- After fetching BibTeX entries, click the **"Copy to Clipboard"** button to copy all entries to your clipboard.

### 6. Restart the Form
- Click the **"Restart"** button to clear all input and output fields, resetting the application for new entries.

### 7. Exit the Application
- Click the **"Exit Application"** button to close the application.

---

## Example

### Input
Enter the following DOIs into the input field:
```
10.1000/xyz123
10.1016/j.scitotenv.2020.141584
```

### Output (when **Include Abstract** is unchecked):
```bibtex
@article{xyz123,
  author = {Author Name},
  title = {Example Article},
  journal = {Journal Name},
  year = {2020},
  doi = {10.1000/xyz123}
}

@article{scitotenv2020,
  author = {Another Author},
  title = {Another Example},
  journal = {Science of the Total Environment},
  year = {2020},
  doi = {10.1016/j.scitotenv.2020.141584}
}
```

---

## Installation and Setup

### Windows Users:
Easily navigate to the `release` here in the **right section**, download the exe file and run it in one click! or if you are interested in using it as *.py file, follow the below instruction

### Prerequisites
- Python 3.7 or higher installed on your system.
- Libraries: `requests`, `Pillow`.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AhsanKhodami/doi2bibtex.git
   ```
2. Navigate to the application directory:
   ```bash
   cd doi2bibtex
   ```
3. Install the required Python libraries:
   ```bash
   pip install requests pillow
   ```

### Running the Application
Run the Python script to launch the GUI:
```bash
python doifetch2.py
```

---

## Contribution

Contributions are welcome! If you encounter issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/AhsanKhodami/doi2bibtex).

---

## Credits

- Developed and maintained by [Ahsan Khodami](https://khodami.site).
- Logos and design inspired by [Khodami.site](https://khodami.site).

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
