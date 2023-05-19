import os
import argparse
import PyPDF2

def set_hide_toolbars_flags(input_pdf_path, output_pdf_path):
    # Open PDF file
    with open(input_pdf_path, 'rb') as file:
        # Create reader and writer for manipulating the PDF
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # The flags for showing or hiding toolbars, menus, etc are in the PDF trailer, under /Root/ViewerPreferences/.
        # If there is no /ViewerPreferences subdirectory, you have to create one.
        catalog = reader.trailer['/Root']
        if '/ViewerPreferences' not in catalog:
            catalog.update({PyPDF2.generic.create_string_object('/ViewerPreferences'): PyPDF2.generic.DictionaryObject()})

        # Create the flags for hiding toolbars, menus, etc.
        viewer_preferences = catalog['/ViewerPreferences']
        viewer_preferences.update({
            PyPDF2.generic.create_string_object('/HideToolbar'): PyPDF2.generic.BooleanObject(True),
            PyPDF2.generic.create_string_object('/HideMenubar'): PyPDF2.generic.BooleanObject(True),
            PyPDF2.generic.create_string_object('/HideWindowUI'): PyPDF2.generic.BooleanObject(True),
        })

        # Copy all the pages from the input to the output
        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])

        # Open the output PDF file and write the modified PDF to it
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

def main():
    # Create a parser so the program can accept the PDF filename as a command line argument.
    parser = argparse.ArgumentParser(description='Set PDF viewer preferences to hide toolbars, menubar, and window UI.')
    parser.add_argument('input_pdf_filename', type=str, help='Name of the input PDF file.')

    # Designate the absolute file paths for the input and output files.
    # The printpdf program will seen the raw PDF to "S:\drawings\out\raw", where the fixpdfview program will pick it up.
    # The fixpdfview program will drop its output to "S:\drawings\out", where the MovePDF program can run normally.
    args = parser.parse_args()
    input_pdf_path = f"S:\\drawings\\out\\raw\\{args.input_pdf_filename}"
    output_pdf_path = f"S:\\drawings\\out\\{args.input_pdf_filename}"

    # Check to ensure the PDF has actually been placed in "S:\drawings\out\raw" before attempting to set flags.
    if os.path.exists(input_pdf_path):
        set_hide_toolbars_flags(input_pdf_path, output_pdf_path)
    else:
        print(f"Error: The input PDF file '{input_pdf_path}' does not exist.")

    # Remove the raw PDF from "out\raw"
    try:
        os.remove(input_pdf_path)
        print("% s removed successfully." % input_pdf_path)
    except OSError as error:
        print(error)
        print("% s cannot be removed." % input_pdf_path)

if __name__ == '__main__':
    main()
