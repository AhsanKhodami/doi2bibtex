<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin: 20px;
        }
        .column {
            flex: 50%;
            padding: 20px;
            box-sizing: border-box;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .header img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
        }
        .header h1 {
            margin: 10px 0;
        }
        .header a {
            text-decoration: none;
            color: #007BFF;
        }
        .header a:hover {
            text-decoration: underline;
        }
        .badge {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .image-container {
            text-align: center;
            margin-bottom: 20px;
        }
        .image-container img {
            max-width: 100%;
            height: auto;
        }
        .content {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .content h2 {
            border-bottom: 2px solid #007BFF;
            padding-bottom: 10px;
        }
        .content details {
            margin-bottom: 20px;
        }
        .content details summary {
            font-weight: bold;
            cursor: pointer;
        }
        .content ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        .content code {
            background: #f1f1f1;
            padding: 5px;
            border-radius: 4px;
            display: block;
            margin: 10px 0;
        }
        .content pre {
            background: #f1f1f1;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="column">
        <div class="header">
            <img src="https://raw.githubusercontent.com/AhsanKhodami/doi2bibtex/refs/heads/main/mainapplication.png" alt="DOI2BibTeX Fetcher">
            <h1>DOI2BibTeX Fetcher</h1>
            <a href="https://ahsankhodami.github.io/doi2bibtex/"><img src="https://image.flaticon.com/icons/png/512/1946/1946488.png" alt="Website Icon" width="20"> Project Website</a>
            <div class="badge">
                [![DOI](https://zenodo.org/badge/912144751.svg)](https://doi.org/10.5281/zenodo.14599850)
            </div>
        </div>
        <div class="content">
            <h2>Features</h2>
            <ul>
                <li>Fetch BibTeX entries for one or more DOIs.</li>
                <li>Optionally include or exclude the abstract from BibTeX entries.</li>
                <li>Copy fetched BibTeX entries directly to the clipboard for easy use.</li>
                <li>Restart the application to input new DOIs.</li>
                <li>Save BibTeX references to a `.bib` file.</li>
                <li><strong>Auto-Save</strong>: Automatically save BibTeX entries after fetching.</li>
                <li><strong>Select Save Location</strong>: You can now choose the location to save the file.</li>
                <li>Clean and modern GUI for a seamless user experience.</li>
            </ul>
            <h2>Version 3.0.1</h2>
            <details>
                <summary><strong>What's New in Version 3.0.0?</strong></summary>
                <ul>
                    <li><strong>Auto-Save</strong>: A new feature that automatically saves the fetched BibTeX entries after every fetch, making the process faster and more efficient.</li>
                    <li><strong>Select Save Location</strong>: Users can now choose where to save the `.bib` file. Once selected, the location will be remembered for future saves.</li>
                    <li><strong>Improved Layout</strong>: The checkboxes for "Include Abstract" and "Auto-Save" have been aligned horizontally, offering a more compact and neat layout.</li>
                    <li><strong>Updated Icons</strong>: The application now features new icons for the control buttons, enhancing the overall visual appeal.</li>
                    <li><strong>Bug Fixes</strong>: Several minor bugs have been fixed to improve the application's performance and stability.</li>
                    <li><strong>Check Saving</strong>: The application checks if the file is saved or not and if not saved, it will ask the user to save the file before closing the application.</li>
                    <li><strong>Progress Bar</strong>: A progress bar is added to show the progress of fetching the BibTeX entries.</li>
                </ul>
            </details>
        </div>
    </div>
    <div class="column">
        <div class="content">
            <h2>How to Use</h2>
            <ol>
                <li><strong>Launch the Application</strong><br>
                    Upon launching, the GUI displays:
                    <ul>
                        <li><strong>Header</strong>: Application logo, title, and links to the GitHub repository and Google Scholar profile.</li>
                        <li><strong>DOI Input Field</strong>: Enter one or more DOIs (separated by space, comma, or new lines).</li>
                        <li><strong>Abstract Option</strong>: Checkbox to include/exclude abstracts.</li>
                        <li><strong>Control Buttons</strong>: Fetch BibTeX, copy to clipboard, restart, save to file, or exit.</li>
                        <li><strong>Output Field</strong>: Displays fetched BibTeX entries.</li>
                    </ul>
                </li>
                <li><strong>Enter DOIs</strong><br>
                    Input one or more DOIs using these formats:
                    <ul>
                        <li>Space-separated: <code>10.1234/example1 10.5678/example2</code></li>
                        <li>Comma-separated: <code>10.1234/example1, 10.5678/example2</code></li>
                        <li>Newline-separated:
                            <pre>
10.1234/example1
10.5678/example2
                            </pre>
                        </li>
                    </ul>
                </li>
                <li><strong>Fetch BibTeX</strong><br>
                    Click <strong>"Fetch BibTeX"</strong> to retrieve entries for all valid DOIs. The fetched entries will appear in the output field.
                </li>
                <li><strong>Customize BibTeX</strong><br>
                    Use the <strong>"Include Abstract"</strong> checkbox to control whether abstracts are included in the entries.
                </li>
                <li><strong>Auto-Save (New in Version 3.0.0)</strong><br>
                    Check the <strong>"Auto-save"</strong> option to automatically save the BibTeX entries after fetching. This will eliminate the need for you to manually save the entries.
                </li>
                <li><strong>Save to File (New in Version 2.0.0 and Updated in Version 3.0.0)</strong><br>
                    After fetching the BibTeX entries, click the <strong>"Save to file"</strong> button to save the entries to a `.bib` file on your computer. The application now remembers the location of your last save. If no location is selected, you'll be prompted to choose a save location. A green "Saved!" message will appear next to the <strong>Save</strong> button to confirm the save action.
                </li>
                <li><strong>Restart the Form</strong><br>
                    Click <strong>"Restart"</strong> to clear all input and output fields.
                </li>
            </ol>
            <h2>Example</h2>
            <h3>Input</h3>
            <pre>
10.1000/xyz123
10.1016/j.scitotenv.2020.141584
            </pre>
            <h3>Output (without abstracts)</h3>
            <pre>
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
            </pre>
        </div>
    </div>
</div>

<div class="container">
    <div class="column">
        <div class="content">
            <h2>Installation and Setup</h2>
            <h3>Windows Users</h3>
            <p>Easily navigate to the <strong>release</strong> section here in the <strong>right section</strong> or <a href="https://github.com/AhsanKhodami/doi2bibtex/releases/">click here</a>, download the exe file, and run it with one click! Alternatively, if you prefer to run it as a Python file, follow the instructions below.</p>
            <h3>For Python Users</h3>
            <ol>
                <li>Clone the repository:
                    <pre>git clone https://github.com/AhsanKhodami/doi2bibtex.git</pre>
                </li>
                <li>Navigate to the directory:
                    <pre>cd doi2bibtex</pre>
                </li>
                <li>Install the required libraries:
                    <pre>pip install requests pillow</pre>
                </li>
                <li>Launch the GUI:
                    <pre>python doi2bibtex.py</pre>
                </li>
            </ol>
        </div>
    </div>
    <div class="column">
        <div class="content">
            <h2>Contribution</h2>
            <p>We welcome contributions! If you encounter issues, have feature suggestions, or would like to improve the project, open an issue or submit a pull request via the <a href="https://github.com/AhsanKhodami/doi2bibtex">GitHub repository</a>.</p>
            <h2>Credits</h2>
            <ul>
                <li><strong>Developer</strong>: <a href="https://khodami.site">Ahsan Khodami</a></li>
                <li><strong>Design Inspiration</strong>: <a href="https://khodami.site">Khodami.site</a></li>
            </ul>
            <h2>License</h2>
            <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>
        </div>
    </div>
</div>

</body>
</html>
