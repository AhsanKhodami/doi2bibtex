
# DOI2BibTeX Fetcher

[![DOI](https://zenodo.org/badge/912144751.svg)](https://doi.org/10.5281/zenodo.14599850)

<div align="center">
     <img src="https://raw.githubusercontent.com/AhsanKhodami/doi2bibtex/refs/heads/main/mainapplication.png" alt="DOI2BibTeX Fetcher">
</div>

**DOI2BibTeX Fetcher** is a lightweight, Python-based GUI application designed to fetch BibTeX entries for DOIs (Digital Object Identifiers). With its modern interface and intuitive design, it simplifies citation management by offering customization options such as including/excluding abstracts, saving entries to files, and copying entries to the clipboard.



## **Features**

- Fetch BibTeX entries for one or more DOIs.
- Optionally include or exclude the abstract from BibTeX entries.
- Copy fetched BibTeX entries directly to the clipboard for easy use.
- Restart the application to input new DOIs.
- Save BibTeX references to a `.bib` file.
- **Auto-Save**: Automatically save BibTeX entries after fetching.
- **Select Save Location**: You can now choose the location to save the file.
- Clean and modern GUI for a seamless user experience.



## **Version 3.0.1**

<details>
  <summary><strong>What's New in Version 3.0.0?</strong></summary>


### New Features:
- **Auto-Save**: A new feature that automatically saves the fetched BibTeX entries after every fetch, making the process faster and more efficient.
- **Select Save Location**: Users can now choose where to save the `.bib` file. Once selected, the location will be remembered for future saves.
- **Improved Layout**: The checkboxes for "Include Abstract" and "Auto-Save" have been aligned horizontally, offering a more compact and neat layout.
- **Updated Icons**: The application now features new icons for the control buttons, enhancing the overall visual appeal.
- **Bug Fixes**: Several minor bugs have been fixed to improve the application's performance and stability.
- **check saving** : application checks if the file is saved or not and if not saved, it will ask the user to save the file before closing the application.
- **progress bar** : a progress bar is added to show the progress of fetching the bibtex entries.



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

### 5. **Auto-Save (New in Version 3.0.0)**
- Check the **"Auto-save"** option to automatically save the BibTeX entries after fetching. This will eliminate the need for you to manually save the entries.

### 6. **Save to File (New in Version 2.0.0 and Updated in Version 3.0.0)**
- After fetching the BibTeX entries, click the **"Save to file"** button to save the entries to a `.bib` file on your computer.
- The application now remembers the location of your last save. If no location is selected, you'll be prompted to choose a save location.
- A green "Saved!" message will appear next to the **Save** button to confirm the save action.

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


## **Installation and Setup**

### Windows Users:
Easily navigate to the `release` section here in the **right section** or [🔗click here](https://github.com/AhsanKhodami/doi2bibtex/releases/), download the exe file, and run it with one click! Alternatively, if you prefer to run it as a Python file, follow the instructions below.

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

## **Contribution**

We welcome contributions! If you encounter issues, have feature suggestions, or would like to improve the project, open an issue or submit a pull request via the [GitHub repository](https://github.com/AhsanKhodami/doi2bibtex).


## **Credits**

- **Developer**: [Ahsan Khodami](https://khodami.site)
- **Design Inspiration**: [Khodami.site](https://khodami.site)

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.
