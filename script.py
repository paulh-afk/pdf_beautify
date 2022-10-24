import subprocess

input_folder_path = 'input/'
output_folder_path = 'output/'

file_name = "TP4"

pdf_file = input_folder_path + file_name + '.pdf'

# t: paragraph
# ff2: italic caracters
# Download the font you want (example site: https://fonts.google.com/)
personnalize_css = '''
    .h1,
    .h2,
    .h3 {
      font-family: 'Poppins', sans-serif;
    }

    .t {
      font-family: 'Lato', sans-serif;
    }

    .ff2 {
      font-family: 'Lato', sans-serif;
      font-weight: 700;
    }
  '''


def createHTMLfile():
    return subprocess.call(['pdf2htmlEX', pdf_file, '--embed-css', '0', '--dest-dir', 'output'], )


statusResponse = createHTMLfile()

with open(output_folder_path + file_name + '.css', 'a') as file:
    file.write(personnalize_css)
    file.close()

if statusResponse != 1:
    exit()
