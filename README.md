# **DOI2BibTeX Fetcher**

[![DOI](https://zenodo.org/badge/912144751.svg)](https://doi.org/10.5281/zenodo.14599850)

<div align="center">
  <img src="https://raw.githubusercontent.com/AhsanKhodami/doi2bibtex/refs/heads/main/mainapplication.png" alt="DOI2BibTeX Fetcher">
</div>

**DOI2BibTeX Fetcher** is a lightweight, Python-based GUI application designed to fetch BibTeX entries for DOIs (Digital Object Identifiers). With its modern interface and intuitive design, it simplifies citation management by offering customization options such as including/excluding abstracts, saving entries to files, and copying entries to the clipboard.

---

## **Features**

- Fetch BibTeX entries for multiple DOIs at once.
- Choose whether to include or exclude abstracts in the BibTeX entries.
- Save BibTeX references to `.bib` files for easy management.
- Copy fetched BibTeX entries directly to the clipboard.
- Clean and responsive GUI designed for seamless user experience.
- Restart functionality to reset inputs and outputs for new DOIs.

---

## **Version v2.0.545680**

<details>
  <summary><strong>What’s New in Version 2.0.545680?</strong></summary>

  - **Save BibTeX References**: Users can now save BibTeX entries directly to `.bib` files.
  - **Enhanced User Interface**: Improved button alignment for a more intuitive experience.
  - **Save Confirmation Message**: A green "Saved!" message appears when BibTeX entries are successfully saved to a file.

</details>

---

## **How to Use**

### 1. **Launch the Application**
Upon launching, the GUI displays:
- **Header**: Application logo, title, and links to the GitHub repository and Google Scholar profile.
- **DOI Input Field**: Enter one or more DOIs (separated by space, comma, or new lines).
- **Abstract Option**: Checkbox to include/exclude abstracts.
- **Control Buttons**: Fetch BibTeX, copy to clipboard, restart, save to file, or exit.
- **Output Field**: Displays fetched BibTeX entries.

### 2. **Enter DOIs**
Input one or more DOIs using these formats:
- Space-separated: `10.1234/example1 10.5678/example2`
- Comma-separated: `10.1234/example1, 10.5678/example2`
- Newline-separated:
  ```
  10.1234/example1
  10.5678/example2
  ```

### 3. **Fetch BibTeX**
- Click **"Fetch BibTeX"** to retrieve entries for all valid DOIs.
- The fetched entries will appear in the output field.

### 4. **Customize BibTeX**
- Use the **"Include Abstract"** checkbox to control whether abstracts are included in the entries.

### 5. **Save to File**
- Click **"Save to File"** to save the BibTeX entries to a `.bib` file.
- A green confirmation message will appear when saving is successful.

### 6. **Copy to Clipboard**
- Click **"Copy to Clipboard"** to copy all BibTeX entries to your clipboard.

### 7. **Restart the Form**
- Click **"Restart"** to clear all input and output fields.

---

## **Example**

### Input
```
10.1000/xyz123
10.1016/j.scitotenv.2020.141584
```

### Output (without abstracts):
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

## **Installation and Setup**

### **Windows Users**
To download the `.exe`:
- Go to the [Releases](https://github.com/AhsanKhodami/doi2bibtex/releases) section on GitHub.
- Download the `.exe` file and run it—no Python installation required!

### **For Python Users**
If you'd prefer to run the Python script:
1. Clone the repository:
   ```bash
   git clone https://github.com/AhsanKhodami/doi2bibtex.git
   ```
2. Navigate to the directory:
   ```bash
   cd doi2bibtex
   ```
3. Install the required libraries:
   ```bash
   pip install requests pillow
   ```
4. Launch the GUI:
   ```bash
   python doi2bibtex.py
   ```

---

## **Contribution**

We welcome contributions! If you encounter issues, have feature suggestions, or would like to improve the project, open an issue or submit a pull request via the [GitHub repository](https://github.com/AhsanKhodami/doi2bibtex).

---

## **Credits**

- **Developer**: [Ahsan Khodami](https://khodami.site)
- **Design Inspiration**: [Khodami.site](https://khodami.site)

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.
