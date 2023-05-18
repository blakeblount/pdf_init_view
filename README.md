
# PDF Viewer Preferences Modifier

This Python script modifies the viewer preferences of a given PDF file. It sets the viewer preferences to hide the toolbars, menubar, and window UI when the PDF is opened in a viewer.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

If running as a Python script, the script requires Python 3 and the `PyPDF2` module. You can install `PyPDF2` with pip:

``pip install PyPDF2``

Alternatively, there is a readymade executable file for use on Windows 10 machines with this project's "dist" directory. It is standalone and has no dependencies, so you can put it on your PATH and run it as any other program.

### Usage

To use the script, call the Python file from your command line, passing in the name of the PDF file you wish to modify as an argument:

``python fixpdfview.py file_to_be_fixed.pdf``

To use the executable file, call the program from your command line, passing in the name of the pdf file as before:

``fixpdfview file_to_be_fixed.pdf``

The script will modify the viewer preferences of the input PDF file to hide the toolbars, menubar, and window UI. It then checks to see if the PDF exists with the out\raw folder before modifying it. 

After the modifications, the script writes the changes to a new output PDF file in the 'out' folder, and deletes the original input file.

## Error Handling

If the script cannot find the input PDF file at the specified path, it will print an error message. Similarly, if it fails to remove the input PDF file after the process, it will print an error message.
