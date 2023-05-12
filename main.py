import os
import argparse
import PyPDF2

def set_hide_toolbars_flag(input_pdf_path, output_pdf_path):
    with open(input_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        catalog = reader.trailer['/Root']
        if '/ViewerPreferences' not in catalog:
            catalog.update({PyPDF2.generic.create_string_object('/ViewerPreferences'): PyPDF2.generic.DictionaryObject()})

        viewer_preferences = catalog['/ViewerPreferences']
        viewer_preferences.update({
            PyPDF2.generic.create_string_object('/HideToolbar'): PyPDF2.generic.BooleanObject(True),
            PyPDF2.generic.create_string_object('/HideMenubar'): PyPDF2.generic.BooleanObject(True),
            PyPDF2.generic.create_string_object('/HideWindowUI'): PyPDF2.generic.BooleanObject(True),
        })

        # Copy all the pages from the input to the output
        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

def main():
    parser = argparse.ArgumentParser(description='Set PDF viewer preferences to hide toolbars, menubar, and window UI.')
    parser.add_argument('input_pdf_path', type=str, help='Path to the input PDF file.')

    args = parser.parse_args()

    if os.path.exists(args.input_pdf_path):
        input_file_base, input_file_ext = os.path.splitext(args.input_pdf_path)
        output_pdf_path = f"{input_file_base}_modified{input_file_ext}"
        set_hide_toolbars_flag(args.input_pdf_path, output_pdf_path)
    else:
        print(f"Error: The input PDF file '{args.input_pdf_path}' does not exist.")

if __name__ == '__main__':
    main()
