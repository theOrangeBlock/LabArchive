#gsheets doesnt like empty string (or maybe this is just a python thing)
#so replacing all empty string with N/A

from gsheets import Sheets

sheets = Sheets.from_files('credential.json', 'storage.json')
url = 'https://docs.google.com/spreadsheets/d/1LBaWNrb4opb5k8QVYNUDL3x8LuAIt79q2VbO5nGFP5o/edit#gid=0'
sheet = sheets.get(url)
archive = sheet.get(1443478036)

i = k = 0
while i < archive.nrows:
    while k < archive.ncols:
        if archive.at(i,k) == "":
            sheet[1443478036][i][k] = 'N/A'
        k += 1
    i += 1
