import subprocess

input_folder_path = 'input/'
file_name = "demo.pdf"

pdf_file = input_folder_path + file_name


def createHTMLfile():
    return subprocess.call(['pdf2htmlEX', pdf_file, '--css-filename', 'style.css', '--dest-dir', 'output'], )


statusResponse = createHTMLfile()

if statusResponse != 1:
    exit()
