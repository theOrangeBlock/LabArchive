import gspread
#gc = gspread.service_account(filename='D:\\Programs\\Python\\LabArchive\\credential.json')

gc = gspread.oauth()
url = 'https://docs.google.com/spreadsheets/d/1LBaWNrb4opb5k8QVYNUDL3x8LuAIt79q2VbO5nGFP5o/edit#gid=1443478036'
sheets = gc.open_by_url(url)
ws = sheets.get_worksheet(1)

listOfLists = ws.get_all_values()
i = k = 0
while i < len(listOfLists):
    while k < len(listOfLists[i]):
        if ws.cell(i,k) == '':
            ws.update()
